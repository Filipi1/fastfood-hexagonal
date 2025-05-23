from typing import List, Optional
from modules.order.application.dtos.request_order import RequestOrder
from modules.order.domain.entities.order_entity import OrderEntity, OrderProduct
from modules.order.domain.enums.order_status import OrderStatus
from modules.order.domain.repositories.order_repository import OrderRepository
from modules.products.domain.services.get_all_products_by_codes import (
    GetAllProductsByCodesService,
)
from modules.shared.domain.interfaces.domain_service import DomainService


class CreateOrderService(DomainService):
    def __init__(
        self,
        get_all_products_by_codes_service: GetAllProductsByCodesService,
        order_repository: OrderRepository,
    ):
        self.get_all_products_by_codes_service = get_all_products_by_codes_service
        self.order_repository = order_repository

    async def execute(
        self,
        user_id: Optional[str],
        session_id: Optional[str],
        order_request: List[RequestOrder],
    ) -> OrderEntity:
        products = await self.get_all_products_by_codes_service.execute(
            [request.product_code for request in order_request]
        )
        products_order = [
            OrderProduct.from_product(product, request.quantity)
            for product, request in zip(products, order_request)
        ]
        await self.order_repository.abandon_all_active_orders_for_user(user_id)
        order = OrderEntity(
            user_id=user_id,
            session_id=session_id,
            products=products_order,
            status=OrderStatus.WAITING_PAYMENT,
        )
        return await self.order_repository.create_order(order)

from modules.order.domain.entities.order_entity import OrderEntity
from modules.order.domain.enums.order_status import OrderStatus
from modules.order.domain.repositories.order_repository import OrderRepository
from modules.shared.domain.interfaces.domain_service import DomainService


class CompleteOrderService(DomainService):
    def __init__(self, order_repository: OrderRepository):
        self.__order_repository = order_repository

    async def execute(self, user_id: str, order_id: str) -> OrderEntity:
        order = await self.__order_repository.get_order_by_id(order_id)
        if order is None:
            raise ValueError("Order not found")

        if order.user_id != user_id:
            raise ValueError("User is not allowed to complete this order")

        if order.status != OrderStatus.WAITING_PAYMENT:
            raise ValueError("Order is not waiting for payment")
        
        order.status = OrderStatus.PAID
        await self.__order_repository.update_order_status(order_id, order.status)
        return order


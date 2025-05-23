from typing import List, Optional
from modules.order.application.dtos.request_order import RequestOrder
from modules.order.domain.entities.order_entity import OrderEntity
from modules.order.domain.services.create_order import CreateOrderService
from modules.shared.domain.interfaces.application_service import UseCase


class CreateNewOrderUseCase(UseCase):
    def __init__(self, create_order_service: CreateOrderService):
        self.__create_order_service = create_order_service

    async def process(
        self,
        user_id: Optional[str],
        session_id: Optional[str],
        order_request: List[RequestOrder],
    ) -> OrderEntity:
        return await self.__create_order_service.execute(
            user_id, session_id, order_request
        )

from typing import Optional
from modules.order.domain.entities.order_entity import OrderEntity
from modules.order.domain.services.complete_order import CompleteOrderService
from modules.shared.interfaces import UseCase


class CompleteOrderUseCase(UseCase):
    def __init__(self, complete_order_service: CompleteOrderService):
        self.__complete_order_service = complete_order_service

    async def process(
        self, user_id: Optional[str], session_id: Optional[str], order_id: str
    ) -> OrderEntity:
        return await self.__complete_order_service.execute(
            user_id, session_id, order_id
        )

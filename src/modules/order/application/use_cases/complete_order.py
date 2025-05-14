from modules.order.domain.entities.order_entity import OrderEntity
from modules.order.domain.services.complete_order import CompleteOrderService
from modules.shared.domain.interfaces.application_service import UseCase


class CompleteOrderUseCase(UseCase):
    def __init__(self, complete_order_service: CompleteOrderService):
        self.__complete_order_service = complete_order_service

    async def process(self, user_id: str, order_id: str) -> OrderEntity:
        return await self.__complete_order_service.execute(user_id, order_id)


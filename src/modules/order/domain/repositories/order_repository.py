from gomongo import GoDatabase
from modules.order.domain.entities.order_entity import OrderEntity
from gomongo.adapters import GoRepository
from gomongo.utils.aggregation_builder.operators import GoIn

from modules.order.domain.enums.order_status import OrderStatus


class OrderRepository(GoRepository[OrderEntity]):
    def __init__(self, database: GoDatabase):
        super().__init__(OrderEntity, database)

    async def get_order_by_id(self, id: str) -> OrderEntity:
        return await self.find_one({"_id": id})

    async def get_user_current_order(self, user_id: str) -> OrderEntity:
        return await self.find_one(
            {"user_id": user_id, "status": GoIn([OrderStatus.WAITING_PAYMENT])}
        )

    async def create_order(self, order: OrderEntity) -> OrderEntity:
        return await self.insert_one(order)

    async def update_order_status(self, order_id: str, status: str) -> bool:
        return await self.update({"status": status}, where={"_id": order_id})

    async def abandon_all_active_orders_for_user(self, user_id: str) -> bool:
        return await self.update(
            {"status": OrderStatus.ABANDONED},
            {"user_id": user_id, "status": GoIn([OrderStatus.WAITING_PAYMENT])},
        )

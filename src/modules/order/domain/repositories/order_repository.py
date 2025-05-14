from gomongo import GoDatabase
from modules.order.domain.entities.order_entity import OrderEntity
from gomongo.adapters import GoRepository
from gomongo.utils.aggregation_builder.operators import GoIn

class OrderRepository(GoRepository[OrderEntity]):
    def __init__(self, database: GoDatabase):
        super().__init__(OrderEntity, database)

    async def get_order_by_id(self, id: str) -> OrderEntity:
        return await self.find_one({"_id": id})

    async def get_user_current_order(self, user_id: str) -> OrderEntity:
        return await self.find_one({ "user_id": user_id, "status": GoIn(["waiting_payment"]) })

    async def create_order(self, order: OrderEntity) -> OrderEntity:
        return await self.insert_one(order)

    async def abandon_all_active_orders_for_user(self, user_id: str) -> bool:
        return await self.update({ "status": "abandoned" }, { "user_id": user_id, "status": GoIn(["waiting_payment"]) })
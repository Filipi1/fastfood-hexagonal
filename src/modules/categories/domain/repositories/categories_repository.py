from typing import List, Optional
from gomongo import GoDatabase
from gomongo.adapters import GoRepository

from modules.categories.domain.entities.category_entity import CategoryEntity


class CategoryRepository(GoRepository[CategoryEntity]):
    def __init__(self, database: GoDatabase):
        super().__init__(CategoryEntity, database)

    async def get_category_by_id(self, id: str) -> Optional[CategoryEntity]:
        category = await self.find_one({"_id": id})
        return category

    async def get_categories(self) -> List[CategoryEntity]:
        categories = await self.find({})
        return categories

    async def add_category(self, category: CategoryEntity) -> Optional[CategoryEntity]:
        return await self.insert_one(category)

from typing import Optional
from modules.categories.domain.entities.category_entity import CategoryEntity
from modules.categories.domain.repositories.categories_repository import (
    CategoryRepository,
)
from modules.shared.interfaces import DomainService


class GetCategoryByIdService(DomainService):
    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    async def execute(self, id: str) -> Optional[CategoryEntity]:
        category = await self.category_repository.get_category_by_id(id)
        if not category:
            raise ValueError("Category not found")
        return category

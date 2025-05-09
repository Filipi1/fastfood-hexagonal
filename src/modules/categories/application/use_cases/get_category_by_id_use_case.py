from typing import Optional
from modules.categories.domain.entities.category_entity import CategoryEntity
from modules.categories.domain.services.get_category_by_id_service import (
    GetCategoryByIdService,
)
from modules.shared.domain.interfaces import UseCase


class GetCategoryByIdUseCase(UseCase):
    def __init__(self, get_category_by_id_service: GetCategoryByIdService):
        self.get_category_by_id_service = get_category_by_id_service

    async def process(self, id: str) -> Optional[CategoryEntity]:
        return await self.get_category_by_id_service.execute(id)

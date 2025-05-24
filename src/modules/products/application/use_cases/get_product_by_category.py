from typing import List
from modules.products.domain.entities.product_entity import ProductEntity
from modules.products.domain.services.get_product_by_category_service import (
    GetProductByCategoryService,
)
from modules.shared.interfaces import UseCase


class GetProductByCategoryUseCase(UseCase):
    def __init__(self, get_product_by_category_service: GetProductByCategoryService):
        self.get_product_by_category_service = get_product_by_category_service

    async def process(self, category_id: str) -> List[ProductEntity]:
        return await self.get_product_by_category_service.execute(category_id)

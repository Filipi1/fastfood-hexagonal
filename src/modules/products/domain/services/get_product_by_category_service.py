from typing import List
from modules.products.domain.entities.product_entity import ProductEntity
from modules.products.domain.repositories.product_repository import ProductRepository
from modules.shared.domain.interfaces.domain_service import DomainService


class GetProductByCategoryService(DomainService):
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def execute(self, category_id: str) -> List[ProductEntity]:
        return await self.product_repository.get_products_by_category(category_id)

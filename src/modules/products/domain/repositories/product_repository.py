from typing import List, Optional
from gomongo import GoDatabase
from gomongo.adapters import GoRepository

from modules.products.domain.entities.product_entity import ProductEntity
from gomongo.utils.aggregation_builder.operators import RelationId, GoIn


class ProductRepository(GoRepository[ProductEntity]):
    def __init__(self, database: GoDatabase):
        super().__init__(ProductEntity, database)

    async def get_product_by_code(self, code: str) -> Optional[ProductEntity]:
        product = await self.find_one({"code": code})
        return product

    async def get_products_by_category(self, category_id: str) -> List[ProductEntity]:
        products = await self.find({"category_id": RelationId(category_id)})
        return products

    async def get_products_by_codes(self, codes: list[str]) -> List[ProductEntity]:
        products = await self.find({"code": GoIn(codes)})
        return products

    async def add_product(self, product: ProductEntity) -> Optional[ProductEntity]:
        return await self.insert_one(product)

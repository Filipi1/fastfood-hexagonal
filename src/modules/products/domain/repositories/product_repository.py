from typing import Optional
from gomongo import GoDatabase
from gomongo.adapters import GoRepository

from modules.products.domain.entities.product_entity import ProductEntity


class ProductRepository(GoRepository[ProductEntity]):
    def __init__(self, database: GoDatabase):
        super().__init__(ProductEntity, database)

    async def get_product_by_code(self, code: str) -> Optional[ProductEntity]:
        product = await self.find_one({"code": code})
        return product

    async def add_product(self, product: ProductEntity) -> Optional[ProductEntity]:
        return await self.insert_one(product)

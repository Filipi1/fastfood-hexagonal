from modules.products.domain.entities.product_entity import ProductEntity
from modules.products.domain.repositories.product_repository import ProductRepository
from modules.shared.interfaces import DomainService


class GetProductService(DomainService):
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def execute(self, product_id: str) -> ProductEntity:
        product = await self.product_repository.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found")
        return product

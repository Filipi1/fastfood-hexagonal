from modules.products.domain.entities.product_entity import ProductEntity
from modules.products.domain.repositories.product_repository import ProductRepository
from modules.shared.domain.interfaces.domain_service import DomainService


class GetProductService(DomainService):
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def execute(self, product_code: str) -> ProductEntity:
        return await self.product_repository.get_product_by_code(product_code)

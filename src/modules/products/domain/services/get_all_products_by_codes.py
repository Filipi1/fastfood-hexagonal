from modules.products.domain.entities.product_entity import ProductEntity
from modules.products.domain.repositories.product_repository import ProductRepository
from modules.shared.domain.interfaces.domain_service import DomainService


class GetAllProductsByCodesService(DomainService):
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def execute(self, product_codes: list[str]) -> list[ProductEntity]:
        products = await self.product_repository.get_products_by_codes(product_codes)
        if not products:
            raise ValueError("Products not found")
        return products

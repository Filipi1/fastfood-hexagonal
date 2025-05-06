from modules.products.domain.entities.product_entity import ProductEntity
from modules.products.domain.repositories.product_repository import ProductRepository
from modules.shared.domain.interfaces.domain_service import DomainService


class AddProductService(DomainService):
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def execute(self, product: ProductEntity) -> ProductEntity:
        if not product.validate():
            raise ValueError("Product is not valid")

        product_by_code = await self.product_repository.get_product_by_code(
            product.code
        )
        if product_by_code:
            raise ValueError("Product already exists")

        return await self.product_repository.add_product(product)

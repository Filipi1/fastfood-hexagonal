from modules.products.domain.entities.product_entity import ProductEntity
from modules.products.domain.repositories.product_repository import ProductRepository
from modules.products.exceptions.product_already_exists_exception import (
    ProductAlreadyExistsException,
)
from modules.products.exceptions.product_invalid import ProductInvalidException
from modules.shared.interfaces import DomainService


class AddProductService(DomainService):
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def execute(self, product: ProductEntity) -> ProductEntity:
        if not product.validate_product():
            raise ProductInvalidException()

        product_by_code = await self.product_repository.get_product_by_code(
            product.code
        )
        if product_by_code:
            raise ProductAlreadyExistsException()

        added_product = await self.product_repository.add_product(product)
        if not added_product:
            raise ValueError("Failed to add product")

        return added_product

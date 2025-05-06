from modules.products.adapters.dtos.request_add_product import RequestAddProduct
from modules.products.domain.entities.product_entity import ProductEntity
from modules.products.domain.services.add_product_service import AddProductService
from modules.shared.domain.interfaces import UseCase


class CreateProductUseCase(UseCase):
    def __init__(self, add_product_service: AddProductService):
        self.add_product_service = add_product_service

    async def process(self, request_add_product: RequestAddProduct) -> ProductEntity:
        product = ProductEntity(
            code=request_add_product.code,
            name=request_add_product.name,
            price=request_add_product.price,
        )
        return await self.add_product_service.execute(product)

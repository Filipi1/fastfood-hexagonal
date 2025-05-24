from modules.products.domain.entities.product_entity import ProductEntity
from modules.products.domain.services.get_product_service import GetProductService
from modules.shared.interfaces import UseCase


class GetProductUseCase(UseCase):
    def __init__(self, get_product_service: GetProductService):
        self.get_product_service = get_product_service

    async def process(self, product_code: str) -> ProductEntity:
        return await self.get_product_service.execute(product_code)

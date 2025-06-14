from modules.categories.application.use_cases.get_category_by_id_use_case import (
    GetCategoryByIdUseCase,
)
from modules.products.application.dtos.request_add_product import RequestAddProduct
from modules.products.domain.entities.product_entity import ProductEntity
from modules.products.domain.services.add_product_service import AddProductService
from modules.products.exceptions.product_already_exists_exception import (
    ProductAlreadyExistsException,
)
from modules.shared.interfaces import UseCase
from modules.shared.exceptions.application_exception import ApplicationException


class CreateProductUseCase(UseCase):
    def __init__(
        self,
        add_product_service: AddProductService,
        get_category_by_id_use_case: GetCategoryByIdUseCase,
    ):
        self.__add_product_service = add_product_service
        self.__get_category_by_id_use_case = get_category_by_id_use_case

    async def process(self, request_add_product: RequestAddProduct) -> ProductEntity:
        try:
            category = await self.__get_category_by_id_use_case.process(
                request_add_product.category_id
            )
            if not category:
                raise ApplicationException("Categoria não encontrada.")

            product = ProductEntity(
                code=request_add_product.code,
                name=request_add_product.name,
                price=request_add_product.price,
                category_id=request_add_product.category_id,
            )
            return await self.__add_product_service.execute(product)
        except ProductAlreadyExistsException as already_exists_exception:
            raise ApplicationException(already_exists_exception.message)

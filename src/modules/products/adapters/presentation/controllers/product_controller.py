from http import HTTPMethod

from fastapi import Depends
from modules.authentication.adapters.presentation.dependencies import decode_auth_token
from modules.products.application.dtos.request_add_product import RequestAddProduct
from modules.shared.decorators import (
    FastAPIManager,
    ControllerOptions,
    APIController,
)
from modules.shared.infra.dependency_injector.containers.core_container import (
    CoreContainer,
)


@FastAPIManager.controller("product", ControllerOptions(tags="Product"))
class ProductController(APIController):
    def __init__(self):
        self.__create_product_use_case = CoreContainer.create_product_use_case()
        self.__get_product_use_case = CoreContainer.get_product_use_case()
        self.__get_product_by_category_use_case = (
            CoreContainer.get_product_by_category_use_case()
        )
        super().__init__()

    @FastAPIManager.route(
        "/add",
        method=HTTPMethod.POST,
        dependencies=[Depends(decode_auth_token)],
    )
    async def add(self, request_add_product: RequestAddProduct):
        await self.__create_product_use_case.process(request_add_product)
        return request_add_product

    @FastAPIManager.route(
        "/{code}",
        method=HTTPMethod.GET,
        dependencies=[Depends(decode_auth_token)],
    )
    async def get(self, code: str):
        return await self.__get_product_use_case.process(code)

    @FastAPIManager.route(
        "/category/{id}",
        method=HTTPMethod.GET,
        dependencies=[Depends(decode_auth_token)],
    )
    async def get_by_category(self, id: str):
        return await self.__get_product_by_category_use_case.process(id)

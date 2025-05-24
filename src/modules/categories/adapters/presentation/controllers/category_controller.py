from http import HTTPMethod

from fastapi import Depends
from modules.authentication.adapters.presentation.dependencies import decode_auth_token
from modules.shared.decorators import (
    FastAPIManager,
    ControllerOptions,
    APIController,
)
from modules.shared.infra.dependency_injector.containers.core_container import (
    CoreContainer,
)


@FastAPIManager.controller("category", ControllerOptions(tags="Category"))
class CategoryController(APIController):
    def __init__(self):
        self.__get_category_by_id_use_case = CoreContainer.get_category_by_id_use_case()
        super().__init__()

    @FastAPIManager.route(
        "/{id}",
        method=HTTPMethod.GET,
        dependencies=[Depends(decode_auth_token)],
    )
    async def get_by_id(self, id: str):
        return await self.__get_category_by_id_use_case.process(id)

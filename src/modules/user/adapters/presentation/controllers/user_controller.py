from http import HTTPMethod
from modules.shared.adapters.presentation.decorators import (
    FastAPIManager,
    ControllerOptions,
    APIController,
)
from modules.shared.infra.dependency_injector.containers.core_container import CoreContainer
from modules.user.application.dtos.request_create_user import RequestCreateUser


@FastAPIManager.controller("user", ControllerOptions(tags="User"))
class UserController(APIController):
    def __init__(self):
        self.__create_user_use_case = CoreContainer.create_user_use_case()
        super().__init__()

    @FastAPIManager.route(
        "/signup",
        method=HTTPMethod.POST,
    )
    async def signup(self, request: RequestCreateUser):
        return await self.__create_user_use_case.process(request)

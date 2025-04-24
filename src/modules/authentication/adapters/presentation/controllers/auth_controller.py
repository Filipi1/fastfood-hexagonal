from http import HTTPMethod

from fastapi import HTTPException
from modules.authentication.adapters.dtos import RequestAnonymousLogin, RequestLogin
from dependency_injector.wiring import inject

from modules.infra.dependency_injector.containers import AuthenticationContainer
from modules.shared.adapters.presentation.decorators import (
    FastAPIManager,
    ControllerOptions,
    APIController,
)


@FastAPIManager.controller("auth", ControllerOptions(tags="Authentication"))
class AuthController(APIController):
    @inject
    def __init__(self):
        self.__authenticate_use_case = AuthenticationContainer.authenticate_use_case()
        super().__init__()

    @FastAPIManager.route("/login/anonymous", method=HTTPMethod.POST)
    async def login_anonymous(self, anonymous_data: RequestAnonymousLogin):
        token = await self.__authenticate_use_case.process(anonymous_data)
        if token is None:
            raise HTTPException(status_code=401, detail={"message": "Acesso negado"})
        return {"message": "Autenticado com sucesso", "data": {"token": token}}

    @FastAPIManager.route("/login", method=HTTPMethod.POST)
    async def login(self, login_data: RequestLogin):
        token = await self.__authenticate_use_case.process(login_data)
        if token is None:
            raise HTTPException(status_code=401, detail={"message": "Acesso negado"})
        return {"message": "Autenticado com sucesso", "data": {"token": token}}

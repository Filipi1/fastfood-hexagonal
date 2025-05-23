from http import HTTPMethod, HTTPStatus

from fastapi import HTTPException
from modules.authentication.application.dtos import RequestAnonymousLogin, RequestLogin
from dependency_injector.wiring import inject

from modules.shared.decorators import (
    FastAPIManager,
    ControllerOptions,
    APIController,
)
from modules.shared.infra.dependency_injector.containers.core_container import (
    CoreContainer,
)


@FastAPIManager.controller("auth", ControllerOptions(tags="Authentication"))
class AuthController(APIController):
    @inject
    def __init__(self):
        self.__authenticate_use_case = CoreContainer.authenticate_use_case()
        super().__init__()

    @FastAPIManager.route(
        "/login/anonymous",
        method=HTTPMethod.POST,
        summary="Efetua login anonimo",
        description="Efetua login anonimo",
    )
    async def login_anonymous(self, anonymous_data: RequestAnonymousLogin):
        token = await self.__authenticate_use_case.process(anonymous_data)
        if token is None:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail={"message": "Acesso negado"}
            )
        return {"message": "Autenticado com sucesso", "data": {"token": token}}

    @FastAPIManager.route(
        "/login",
        method=HTTPMethod.POST,
        summary="Efetua login com usuario e senha",
        description="Efetua login com usuario e senha",
    )
    async def login(self, login_data: RequestLogin):
        token = await self.__authenticate_use_case.process(login_data)
        if token is None:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail={"message": "Acesso negado"}
            )
        return {"message": "Autenticado com sucesso", "data": {"token": token}}

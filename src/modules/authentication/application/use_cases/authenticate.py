from typing import Optional
from modules.authentication.application.dtos import RequestAnonymousLogin, RequestLogin
from modules.authentication.domain.services import (
    DoAnonymousAuthenticationService,
    DoAuthenticationService,
)
from modules.shared.domain.interfaces import UseCase


class AuthenticateUseCase(UseCase):
    def __init__(
        self,
        do_anonymous_authentication_service: DoAnonymousAuthenticationService,
        do_authentication_service: DoAuthenticationService,
    ):
        self.__do_anonymous_authentication_service = do_anonymous_authentication_service
        self.__do_authentication_service = do_authentication_service
        super().__init__()

    async def process(
        self, request_login: RequestAnonymousLogin | RequestLogin
    ) -> Optional[str]:
        if isinstance(request_login, RequestAnonymousLogin):
            return await self.__do_anonymous_authentication_service.execute(
                request_login=request_login
            )
        return await self.__do_authentication_service.execute(
            request_login=request_login
        )

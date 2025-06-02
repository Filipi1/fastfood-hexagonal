from typing import Optional
from modules.authentication.application.dtos import RequestLogin
from modules.authentication.adapters.security.jwt.jwt_service import JWTService
from modules.authentication.application.dtos.auth_token_data import AuthTokenData
from modules.shared.interfaces import DomainService
from modules.shared.utils.encrypter.encrypter import Encrypter
from modules.user.domain.services.get_user_by_email_and_password import (
    GetUserByEmailService,
)


class DoAuthenticationService(DomainService):
    def __init__(
        self,
        jwt_service: JWTService,
        get_user_by_email_service: GetUserByEmailService,
    ) -> None:
        self.__jwt_service = jwt_service
        self.__get_user_by_email_service = get_user_by_email_service
        super().__init__()

    async def execute(self, request_login: RequestLogin) -> Optional[str]:
        user = await self.__get_user_by_email_service.execute(request_login.email)
        if not user:
            raise ValueError("Usuário não encontrado")

        if not Encrypter.verify(request_login.password, user.password):
            raise ValueError("Usuário ou senha inválidos")

        token = self.__jwt_service.encode(
            AuthTokenData(
                id=user.id,
                session_id=user.session_id,
                name=user.name,
                email=user.email,
                document=user.document,
            ).model_dump()
        )
        return token

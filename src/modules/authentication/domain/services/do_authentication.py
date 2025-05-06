import hashlib
from typing import Optional
from modules.authentication.application.dtos import RequestLogin
from modules.authentication.adapters.security.jwt.jwt_service import JWTService
from modules.shared.domain.interfaces import DomainService
from modules.user.domain.services.get_user_by_email_and_password import (
    GetUserByEmailAndPasswordService,
)


class DoAuthenticationService(DomainService):
    def __init__(
        self,
        jwt_service: JWTService,
        get_user_by_email_and_password_service: GetUserByEmailAndPasswordService,
    ) -> None:
        self.__jwt_service = jwt_service
        self.__get_user_by_email_and_password_service = (
            get_user_by_email_and_password_service
        )
        super().__init__()

    async def execute(self, request_login: RequestLogin) -> Optional[str]:
        encrypted_password = hashlib.sha256(
            request_login.password.encode("utf-8")
        ).hexdigest()
        user = await self.__get_user_by_email_and_password_service.execute(
            request_login.email, encrypted_password
        )
        if user:
            token = self.__jwt_service.encode(user.model_dump())
            return token
        return None

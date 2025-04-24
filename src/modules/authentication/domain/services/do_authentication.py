from typing import Optional
from modules.authentication.adapters.dtos import RequestLogin
from modules.authentication.adapters.security.jwt.jwt_service import JWTService
from modules.authentication.domain.entities import Authentication
from modules.shared.domain.interfaces import DomainService


class DoAuthenticationService(DomainService):
    def __init__(self, jwt_service: JWTService) -> None:
        self.__jwt_service = jwt_service
        super().__init__()

    async def execute(self, request_login: RequestLogin) -> Optional[str]:
        if (
            request_login.email == "admin@admin.com"
            and request_login.password == "admin"
        ):
            authentication = Authentication(
                email=request_login.email, name="Admin", document="12345678901"
            )
            token = self.__jwt_service.encode(authentication.model_dump())
            return token
        return None

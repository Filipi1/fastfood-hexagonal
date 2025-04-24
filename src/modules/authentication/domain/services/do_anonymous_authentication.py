from typing import Optional
from modules.authentication.adapters.dtos import RequestAnonymousLogin
from modules.authentication.adapters.security.jwt.jwt_service import JWTService
from modules.authentication.domain.entities import Authentication
from modules.shared.domain.interfaces import DomainService


class DoAnonymousAuthenticationService(DomainService):
    def __init__(self, jwt_service: JWTService) -> None:
        self.__jwt_service = jwt_service
        super().__init__()

    async def execute(self, request_login: RequestAnonymousLogin) -> Optional[str]:
        authentication = Authentication(
            name=request_login.name, document=request_login.document
        )
        token = self.__jwt_service.encode_no_auth(authentication.model_dump())
        return token

from typing import Optional
from modules.shared.domain.interfaces.domain_service import DomainService
from modules.user.domain.entities.user import User
from modules.user.domain.repositories.user_repository import UserRepository


class GetUserByEmailAndPasswordService(DomainService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, email: str, password: str) -> Optional[User]:
        return await self.user_repository.get_user_by_email_and_password(
            email, password
        )

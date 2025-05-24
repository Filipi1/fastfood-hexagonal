from typing import Optional
from modules.shared.interfaces import DomainService
from modules.user.domain.entities.user import User
from modules.user.domain.repositories.user_repository import UserRepository


class GetUserByEmailService(DomainService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, email: str) -> Optional[User]:
        return await self.user_repository.get_user_by_email(email)

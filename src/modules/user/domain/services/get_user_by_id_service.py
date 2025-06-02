from typing import Optional
from modules.shared.interfaces import DomainService
from modules.user.domain.entities.user import User
from modules.user.domain.repositories.user_repository import UserRepository


class GetUserByIdService(DomainService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_id: int) -> Optional[User]:
        return await self.user_repository.get_user_by_id(user_id)

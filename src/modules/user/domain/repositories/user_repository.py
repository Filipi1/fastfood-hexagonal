from typing import Optional
from gomongo import GoDatabase
from gomongo.adapters import GoRepository
from modules.user.domain.entities.user import User


class UserRepository(GoRepository[User]):
    def __init__(self, database: GoDatabase):
        super().__init__(User, database)

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        user = await self.find_one({"_id": user_id})
        return user

    async def get_user_by_email_and_password(
        self, email: str, password: str
    ) -> Optional[User]:
        user = await self.find_one({"email": email, "password": password})
        return user

    async def get_user_by_email(self, email: str) -> Optional[User]:
        return await self.find_one({"email": email})

    async def create_user(self, user: User) -> User:
        return await self.insert_one(user)

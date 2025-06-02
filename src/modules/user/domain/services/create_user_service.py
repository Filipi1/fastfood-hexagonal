from modules.shared.utils.encrypter.encrypter import Encrypter
from modules.user.domain.entities.user import User
from modules.user.domain.repositories.user_repository import UserRepository
from modules.shared.interfaces import DomainService
from modules.user.exceptions.user_already_exists_exception import (
    UserAlreadyExistsException,
)
from modules.user.exceptions.user_invalid_data_exception import UserInvalidDataException


class CreateUserService(DomainService):
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository
        super().__init__()

    async def execute(self, user: User) -> User:
        existing_user = await self.__user_repository.get_user_by_email(user.email)
        if existing_user:
            raise UserAlreadyExistsException()

        user.password = Encrypter.encrypt(user.password)
        if not user.validate_user():
            raise UserInvalidDataException()

        return await self.__user_repository.create_user(user)

from modules.shared.exceptions.application_exception import ApplicationException
from modules.user.application.dtos.request_create_user import RequestCreateUser
from modules.user.domain.entities.user import User
from modules.user.domain.services.create_user_service import CreateUserService
from modules.shared.interfaces import UseCase
from modules.user.exceptions.user_already_exists_exception import (
    UserAlreadyExistsException,
)
from modules.user.exceptions.user_invalid_data_exception import UserInvalidDataException


class CreateUserUseCase(UseCase):
    def __init__(self, create_user_service: CreateUserService):
        self.__create_user_service = create_user_service

    async def process(self, request_create_user: RequestCreateUser) -> User:
        try:
            user = User(**request_create_user.model_dump())
            return await self.__create_user_service.execute(user)
        except UserAlreadyExistsException as already_exists_exception:
            raise ApplicationException(already_exists_exception.message)
        except UserInvalidDataException as invalid_data_exception:
            raise ApplicationException(invalid_data_exception.message)

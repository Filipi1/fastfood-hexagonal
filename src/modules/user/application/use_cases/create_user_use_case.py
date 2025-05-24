from modules.user.application.dtos.request_create_user import RequestCreateUser
from modules.user.domain.entities.user import User
from modules.user.domain.services.create_user_service import CreateUserService
from modules.shared.interfaces import UseCase


class CreateUserUseCase(UseCase):
    def __init__(self, create_user_service: CreateUserService):
        self.__create_user_service = create_user_service

    async def process(self, request_create_user: RequestCreateUser) -> User:
        user = User(
            **request_create_user.model_dump()
        )
        return await self.__create_user_service.execute(user)
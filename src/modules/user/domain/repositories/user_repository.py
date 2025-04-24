from modules.user.domain.entities import User


class UserRepository:
    def get_user(self, id: int):
        return User(id=id, name="John Doe", email="john.doe@example.com")

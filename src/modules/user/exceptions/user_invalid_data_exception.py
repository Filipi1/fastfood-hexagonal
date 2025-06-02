from modules.shared.exceptions.domain_exception import DomainException


class UserInvalidDataException(DomainException):
    def __init__(self):
        super().__init__("Dados do usuário inválidos.")

from modules.shared.exceptions.domain_exception import DomainException


class UserAlreadyExistsException(DomainException):
    def __init__(self):
        super().__init__("Usuário já cadastrado.")

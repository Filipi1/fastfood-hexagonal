from modules.shared.exceptions.domain_exception import DomainException


class ProductAlreadyExistsException(DomainException):
    def __init__(self):
        super().__init__("O produto já existe.")

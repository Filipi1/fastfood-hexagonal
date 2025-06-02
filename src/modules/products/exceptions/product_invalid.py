from modules.shared.exceptions.domain_exception import DomainException


class ProductInvalidException(DomainException):
    def __init__(self):
        super().__init__("Produto inválido.")

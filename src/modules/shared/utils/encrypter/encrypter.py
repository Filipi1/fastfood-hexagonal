from passlib.context import CryptContext


class Encrypter:
    @staticmethod
    def encrypt(value: str) -> str:
        return CryptContext(schemes=["bcrypt"], deprecated="auto").hash(value)

    @staticmethod
    def verify(value: str, hashed_value: str) -> bool:
        return CryptContext(schemes=["bcrypt"], deprecated="auto").verify(
            value, hashed_value
        )

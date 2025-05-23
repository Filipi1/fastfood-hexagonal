from datetime import timedelta
from typing import Dict, Optional
import uuid


from jose import JWTError, jwt, ExpiredSignatureError
from modules.shared.application.helpers.date_helper import DateHelper


class JWTService:
    def __init__(
        self,
        secret_key: str,
        algorithm: str,
        secret_key_no_auth: str,
        algorithm_no_auth: str,
    ):
        self.__secret_key = secret_key
        self.__algorithm = algorithm
        self.__secret_key_no_auth = secret_key_no_auth
        self.__algorithm_no_auth = algorithm_no_auth

    def generate_session_id(self) -> str:
        return str(uuid.uuid4())

    def encode(self, data: dict) -> str:
        data_to_encode = data.copy()
        data_to_encode.update({"session_id": self.generate_session_id()})
        expiration_date = DateHelper.create_expiration_date(timedelta(minutes=5))
        data_to_encode.update({"exp": int(expiration_date.timestamp())})
        return jwt.encode(data_to_encode, self.__secret_key, algorithm=self.__algorithm)

    def encode_no_auth(self, data: dict) -> str:
        data_to_encode = data.copy()
        data_to_encode.update({"session_id": self.generate_session_id()})
        expiration_date = DateHelper.create_expiration_date(timedelta(minutes=5))
        data_to_encode.update(
            {"exp": int(expiration_date.timestamp()), "etype": "no_auth"}
        )
        return jwt.encode(
            data_to_encode,
            self.__secret_key_no_auth,
            algorithm=self.__algorithm_no_auth,
        )

    def decode_token(self, token: str) -> Optional[Dict]:
        try:
            return jwt.decode(token, self.__secret_key, algorithms=[self.__algorithm])
        except ExpiredSignatureError:
            return None
        except JWTError:
            return self.__decode_token_no_auth(token)

    def __decode_token_no_auth(self, token: str) -> Optional[Dict]:
        try:
            return jwt.decode(
                token, self.__secret_key_no_auth, algorithms=[self.__algorithm_no_auth]
            )
        except JWTError:
            return None

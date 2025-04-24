from typing import Optional
from pydantic import BaseModel


class AuthTokenData(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    document: Optional[str] = None

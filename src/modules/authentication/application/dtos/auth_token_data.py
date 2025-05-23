from typing import Optional
from pydantic import BaseModel


class AuthTokenData(BaseModel):
    id: Optional[str] = None
    session_id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    document: Optional[str] = None

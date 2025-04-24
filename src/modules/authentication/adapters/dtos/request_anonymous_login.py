from typing import Optional
from pydantic import BaseModel, Field


class RequestAnonymousLogin(BaseModel):
    name: str = Field(description="Nome do usuário")
    document: Optional[str] = Field(None, description="Documento do usuário")

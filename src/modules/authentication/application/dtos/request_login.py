from pydantic import BaseModel, Field


class RequestLogin(BaseModel):
    email: str = Field(description="Email do usuário")
    password: str = Field(description="Senha do usuário")

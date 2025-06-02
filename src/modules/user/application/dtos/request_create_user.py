from pydantic import BaseModel, Field, EmailStr


class RequestCreateUser(BaseModel):
    name: str = Field(description="Nome do usuário", min_length=3)
    email: EmailStr = Field(description="Email do usuário")
    password: str = Field(description="Senha do usuário", min_length=6)

from pydantic import BaseModel, Field


class RequestAddProduct(BaseModel):
    code: str = Field(description="Código do produto", min_length=1)
    name: str = Field(description="Nome do produto", min_length=1)
    price: float = Field(description="Preço do produto")
    category_id: str = Field(description="ID da categoria do produto")

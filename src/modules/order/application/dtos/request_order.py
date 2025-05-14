from pydantic import BaseModel, Field


class RequestOrder(BaseModel):
    product_code: str = Field(description="Código do produto", min_length=1)
    quantity: int = Field(description="Quantidade do produto", default=1)

from pydantic import BaseModel, Field


class RequestOrder(BaseModel):
    products: list[str] = Field(description="Lista de produtos", min_length=1)

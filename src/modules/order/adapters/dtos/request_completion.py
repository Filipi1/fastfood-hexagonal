from pydantic import BaseModel, Field


class RequestOrderCompletion(BaseModel):
    payment_token: str = Field(description="Token do pagamento", min_length=1)

from datetime import datetime
from typing import Dict, List, Literal, Optional
from gomongo.ports import GoEntity
from pydantic import Field, field_validator, model_validator
from gomongo.decorators import GoCollection
from pydantic import BaseModel

from modules.products.domain.entities.product_entity import ProductEntity

class OrderProduct(BaseModel):
    name: str
    price: float
    quantity: int = Field(default=1)
    total_price: float = Field(default=0)
    total_discount: float = Field(default=0)
    total_price_with_discount: float = Field(default=0)

    def get_total_price(self) -> float:
        return self.total_price
    
    def get_total_discount(self) -> float:
        return self.total_discount

    @model_validator(mode="before")
    def calculate_prices(cls, data):
        data["total_price"] = data["price"] * data["quantity"]
        data["total_price_with_discount"] = data["total_price"] - data["total_discount"]
        return data

    @staticmethod
    def from_product(product: ProductEntity, quantity: int = 1) -> "OrderProduct":
        return OrderProduct(
            name=product.name,
            price=product.price,
            quantity=quantity,
            total_discount=product.discount,
        )

@GoCollection("orders")
class OrderEntity(GoEntity):
    status: Literal["waiting_payment", "paid", "cancelled"]
    user_id: str
    products: list[OrderProduct]
    total_price: float = Field(default=0)
    total_products: int = Field(default=0)
    total_discounts: float = Field(default=0)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[List[Dict]] = Field(default=[])


    @model_validator(mode='after')
    def compute_total_price(self) -> 'OrderEntity':
        self.total_price = sum(p.price for p in self.products)
        self.total_products = len(self.products)
        return self
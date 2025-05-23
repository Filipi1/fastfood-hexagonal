from datetime import datetime
from typing import Dict, List, Optional
from gomongo.ports import GoEntity
from pydantic import Field, model_validator
from gomongo.decorators import GoCollection
from pydantic import BaseModel

from modules.order.domain.enums.order_status import OrderStatus
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
        data["total_price"] = round(float(data["price"] * data["quantity"]), 2)
        data["total_price_with_discount"] = round(
            float(data["total_price"] - data["total_discount"]), 2
        )
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
    status: OrderStatus
    user_id: Optional[str] = None
    session_id: Optional[str] = Field(default=None)
    products: list[OrderProduct]
    total_price: float = Field(default=0)
    total_products: int = Field(default=0)
    total_discounts: float = Field(default=0)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[List[Dict]] = Field(default=[])

    @model_validator(mode="after")
    def compute_total_price(self) -> "OrderEntity":
        self.total_price = round(float(sum(p.total_price for p in self.products)), 2)
        self.total_products = len(self.products)

        if not self.session_id and not self.user_id:
            raise ValueError("Session or user ID is required")

        return self

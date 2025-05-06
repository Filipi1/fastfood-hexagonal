from datetime import datetime
from typing import Dict, List, Literal, Optional
from gomongo.ports import GoEntity
from pydantic import Field


class OrderProduct(GoEntity):
    name: str
    price: float
    quantity: int
    total_price: float
    total_discount: float
    total_price_with_discount: float


class OrderResume(GoEntity):
    total_price: float
    total_products: int
    total_items: int
    total_discounts: int
    products: list[OrderProduct]


class OrderEntity(GoEntity):
    status: Literal["waiting_payment", "paid", "cancelled"]
    user_id: int
    products: list[str]
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[List[Dict]] = Field(default=[])

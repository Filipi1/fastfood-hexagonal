from datetime import datetime
from typing import Dict, List, Optional
from gomongo.ports import GoEntity
from pydantic import Field
from gomongo.decorators import GoCollection


@GoCollection("products")
class ProductEntity(GoEntity):
    code: str
    name: str
    price: float
    discount: float = Field(default=0)
    active: bool = Field(default=True)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[List[Dict]] = Field(default=[])

    def validate(self) -> bool:
        if self.code is None or self.name is None or self.price is None:
            return False

        if self.price < 0:
            return False

        if self.discount < 0 or self.discount > self.price:
            return False

        return True

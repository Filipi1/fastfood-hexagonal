from datetime import datetime
from typing import Dict, List, Optional
from gomongo.decorators import GoCollection
from gomongo.ports import GoEntity
from pydantic import Field


@GoCollection("categories")
class CategoryEntity(GoEntity):
    name: str
    image: Optional[str] = None
    active: bool = Field(default=True)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[List[Dict]] = Field(default=[])

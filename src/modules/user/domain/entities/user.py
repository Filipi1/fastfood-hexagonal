from datetime import datetime
from typing import Optional
from gomongo.ports import GoEntity
from gomongo.decorators import GoCollection
from pydantic import Field


@GoCollection("users")
class User(GoEntity):
    session_id: Optional[str] = None
    name: str
    password: Optional[str] = Field(default=None)
    document: Optional[str] = None
    email: Optional[str] = None
    active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    @property
    def is_anonymous(self) -> bool:
        return self.id is None

    def validate_user(self) -> bool:
        if not self.name or not self.email or not self.password:
            return False
        return True

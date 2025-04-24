from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int] = None
    name: str
    document: Optional[str] = None
    email: Optional[str] = None

    @property
    def is_anonymous(self) -> bool:
        return self.id is None

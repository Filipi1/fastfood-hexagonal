from typing import Optional
from gomongo.ports import GoEntity
from gomongo.decorators import GoCollection


@GoCollection("users")
class User(GoEntity):
    name: str
    document: Optional[str] = None
    email: Optional[str] = None

    @property
    def is_anonymous(self) -> bool:
        return self.id is None

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


@dataclass
class ControllerOptions:
    tags: Optional[List[str | Enum]] | str = None
    version: str = "v1"

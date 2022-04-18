from dataclasses import dataclass, field
from typing import Optional
@dataclass(frozen=True)
class Person:
    id:int
    name:str = field(hash=False, compare=False)
    favorite_color: Optional[str] = field(default_factory=lambda :None, hash=False, compare=False)

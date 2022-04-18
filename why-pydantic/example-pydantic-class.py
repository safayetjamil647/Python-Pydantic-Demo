from typing import Optional
from pydantic import BaseModel, validator, PositiveInt
class Person(BaseModel):
    class Config:
        allow_mutation = False
        validate_all = True
    id:PositiveInt
    name:str
    favorite_color: Optional[str] = None
    @validator('name')
    def validate_name(cls, v):
        if not v:
            raise ValueError("Name can't be an empty")
        return v
    def __hash__(self):
        return hash(self.id)
    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return self.id == other.id
        return False
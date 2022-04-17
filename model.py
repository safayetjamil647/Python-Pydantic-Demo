from enum import Enum
from pydantic import BaseModel, Field





class MainModel(BaseModel):
    snap: int = Field(
        42,
        title='The Snap',
        description='this is the value of snap',
        gt=30,
        lt=50,
    )

    class Config:
        title = 'Main'

# this is equivalent to json.dumps(MainModel.schema(), indent=2):

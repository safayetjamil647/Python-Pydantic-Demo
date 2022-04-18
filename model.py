from enum import Enum
from pydantic import BaseModel, Field

# data = {
#     "name": "Michael Kennedy",
#     "age": "28",
#     "location": {
#         "city": "Portland",
#         "state": "Oregon",
#     },
#     "bike": "Ktm Duke",
#     "rides": [7, 103, 22, "70", 100]
# }
# class User:
#     name: str
#     location = None
#     bike: str
#     rides: list[int]= []




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



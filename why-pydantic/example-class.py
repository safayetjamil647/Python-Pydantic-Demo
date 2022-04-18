from typing import Optional
class Person(object):
    def __init__(self, id:int, name:str, favorite_color:Optional[str] = None):
        self.id = id
        self.name = name
        self.favorite_color = favorite_color
    def __repr__(self):
        return "<{} id:{} name:{}>".format(self.__class__.__name__, self.id, self.name)
    def __hash__(self):
        return hash(self.id)
    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return self.id == other.id
        return False

class User:
    # class attributes
    types = "user"

    # instance attribute

    def __init__(self, name, age):
        self.name = name

        self.age = age


# instantiate the user class
jhon = User("Jhon", 20)
jamil = User("Jamil", 26)

print(" My details is {}".format(jhon.__class__.types))
print(" My details is {}".format(jamil.__class__.types))

# access the instance attributes
print("{} is {} years old".format(jhon.name, jhon.age))
print("{} is {} years old".format(jamil.name, jamil.age))

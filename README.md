## Python OOP and Pydantic Overview
- Basics of python and python OOP
- Pydantic and It's usage
- Simple CRUD Operation without framework 
- Python and it's library's

Not so basic not too advance POC 


## OOP Section

This section is for python OOP learning and it's outcome :

### Class (1)
A class is a blueprint for the object.

We can think of class as a sketch of a user with labels.
It contains all the details about the name, address , emails etc.
Based on these descriptions, we can study about the user. 
Here, a user is an object in oop folder class.py file

```
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
# class attributes
print(" My details is {}".format(jhon.__class__.types))
print(" My details is {}".format(jamil.__class__.types))

#  instance attributes
print("{} is {} years old".format(jhon.name, jhon.age))
print("{} is {} years old".format(jamil.name, jamil.age))
```

In that program 

```class user``` means 
the name of the class . And ```types = "user"``` means it is the characteristics of object.This is called attributes.
Init is the initializer method to create the object of the class.It runs after object creation.
Instantiation means create real instance such as class objects here.After that the code blocks below showed how to 
access class and instance attributes.

```self``` The self is used to represent the instance of the class. With this keyword, you can access the attributes 
and methods of the class in python. It binds the attributes with the given arguments.

```__class__``` What is this? This is Dunder Method in python.A Dunder method is a method (that Python knows about),
which has two underscores before it and two underscores after it.

example
```
name = "Trey"
len(name)
4 
```
in this code block use Dunder Method like this ```name.__len__()```


## Pydantic Section

This section is for python Pydantic(library) learning, and it's outcome:

In Class(1) we have learned about what is class and a little dig down.
Now a question in mind may appear that why we will use pydantic library for more optimization .
Let have a look in why pydantic folder . There is three file{example-class, example-dataclass, example-pydantic-class},
those are example for this section.


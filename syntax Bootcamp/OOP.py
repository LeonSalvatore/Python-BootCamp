# Studying python - OOP
# # Python is an object-oriented programming language
# # Almost everything in Python is an object, with its properties and methods
# # A Class is like a blueprint for creating objects
# # An Object is a particular data structure that contains data and methods
# # A Class is a collection of objects
# # A Class is a blueprint for creating objects
# # An Object is an instance of a Class

class MyClass:
    x = 5
    y = "John"
    def myfunc(self):
        print("Hello World")
    # The __init__() function is called automatically every time the class is being used to create a new object
    def __init__(self, name):
        self.name = name
    # The __str__() function is called when you use the print() function on an object
    def __str__(self):
        return f"My name is {self.name}"
    # The __len__() function is called when you use the len() function on an object
    def __len__(self):
        return len(self.name)
    # The __del__() function is called when the object is deleted
    def __del__(self):
        print(f"{self.name} is deleted")
    # The __repr__() function is called when you use the repr() function on an object
    def __repr__(self):
        return f"My name is {self.name}"
    # The __add__() function is called when you use the + operator on an object
    

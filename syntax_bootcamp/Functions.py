""
# Studying python - Functions
# Functions are used to execute a block of code when it is called
# Functions are defined using the def keyword
# A function can take parameters, which are values passed to the function when it is called
# A function can return a value using the return keyword
# A function can have default parameter values, which are used if no value is passed to the function
# A function can have variable-length arguments, which allow you to pass a variable number of arguments to the function
# A function can have keyword arguments, which allow you to pass arguments by name instead of position
# A function can have a docstring, which is a string that describes the function and is used for documentation
# A function can be called using its name followed by parentheses
# A function can be called with or without arguments
# A function can be called with keyword arguments


def my_first_function():
    print("Hello from my first function")


def my_function_with_parameters(name):
    print("Hello " + name)
    
my_function_with_parameters("John")

def my_function_with_default_parameters(name="John"):
    print("Hello " + name)
    
my_function_with_default_parameters()

def function(): 
    print("Hello from function")
    
function()

leon = 'Leon'
leon = 10

print(leon)
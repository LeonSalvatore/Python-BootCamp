
 # Studying python - Variables
# Variables are used to store data values
# In Python, variables are created when you assign a value to it
x = 5
y = "John"
print(x)
print(y)
# Variables do not need to be declared with any particular type and can even change type after they have been set
x = 4
x = "Sally"
print(x)
# Variables with the same name can be used in different scopes
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)
# If you create a variable with the same name inside a function, it will be local and not global
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

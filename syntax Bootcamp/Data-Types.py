# Data Types in Python
#  Python has the following data types built-in by default, in these categories:
#  Text Type:	str
#  Numeric Types:	int, float
#  Sequence Types:	list, tuple, range
#  Mapping Type:	dict
#  Set Types:	set, frozenset
#  Boolean Type:	bool
#  Binary Types:	bytes, bytearray, memoryview
#  None Type:	NoneType
#  Getting the Data Type
#  You can get the data type of any object by using the type() function


y = 5
x = "John"
print(type(x))
print(type(y))
 # Setting the Data Type
    # # In Python, the data type is set when you assign a value to a variable
x = "John"    # str
y = 20      # int
z = 20.5    # float
a = 1j      # complex
b = ["apple", "banana", "cherry"]  # list
c = ("apple", "banana", "cherry")  # tuple
d = range(6)  # range
e = {"name": "John", "age": 36}  # dict
f = {"apple", "banana", "cherry"}  # set
g = frozenset({"apple", "banana", "cherry"})  # frozenset
h = True  # bool
i = b"Hello"  # bytes
j = bytearray(5)  # bytearray
k = memoryview(bytes(5))  # memoryview
l = None  # NoneType
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))


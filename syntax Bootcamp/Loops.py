# Studying python - Loops
#  A loop is used for iterating over a sequence (like a list, tuple, dictionary, set, or string)
#  The for loop in Python is used to iterate over a sequence (list, tuple, dictionary, set, or string)
#  The for loop has a loop variable that takes the value of the item inside the sequence on each iteration
#  The for loop can also be used to iterate over a range of numbers using the range() function
#  The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number
#  The range() function can take one, two, or three arguments
#  The first argument is the starting number, the second argument is the ending number, and the third argument is the step
#  The step is optional and defaults to 1
#  The range() function returns a range object, which is an immutable sequence type
#  The range object can be converted to a list or tuple using the list() or tuple() functions
#  The range object can also be used in a for loop
#  The while loop in Python is used to execute a block of code as long as the condition is true
#  The while loop has a condition that is checked before the block of code is executed
#  The while loop can be used to iterate over a sequence (like a list, tuple, dictionary, set, or string)
#  The while loop can also be used to iterate over a range of numbers using the range() function
#  The while loop can be used to execute a block of code as long as the condition is true
#

for i in range(5):
    break
   # print(i)

names = ["Alice", "Bob", "Charlie"]
for person in names:
    
   # print(person)
   break
    
for index in range(2):
    #print(names[index])
    break

while names[1] != "Alice":
    
    print(names[1])
    break
   
    names[1] = "Bob"
# The break statement is used to exit a loop
# The continue statement is used to skip the current iteration of a loop
# The pass statement is used as a placeholder for future code
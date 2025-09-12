"""
Check data types in python. I have stored two variables like school_objects and scobject1
var: This is a parameter of the function. It represents the actual variable whose type you want to check. 
When you call the function, you pass your data (like school_objects or scobject1) as the argument for var.
var_name: This is another parameter. 
It's a string that represents the name of the variable you want to print out, 
so that the function can produce a message like "school_objects is a list in Python programming" instead of just "It is a list"
"""

import time as t 
school_objects = ["pen", "pencil", "book", "bag"]
print(school_objects)
t.sleep(2)
if isinstance(school_objects, list):
  print("You have a list in Python programming")
elif isinstance(school_objects, int):
  print("You have an integer in Python programming")
elif isinstance(school_objects, str):
  print("You have a string in Python programming")
elif isinstance(school_objects, bool):
  print("You have a boolean in Python programming")
else:
  print("You need to check the datatypes syntax..")
t.sleep(1)
print(f"going to see list constructor")
print("")
scobject1 = list(("pencil","pen","book"))
print(type(scobject1))
if isinstance(scobject1, list):
  print("You have a python constructor in the program")
else:
  print("Nothing is datatypes here..")

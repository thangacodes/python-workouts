import time
import sys

# You can declare variables like this:-

# a = "Td"
# b = "Ess"
# c = "Vedhu"
# d = "Anv"

# Printing declared variables using f-string:-

# print(f"My family members are: {a}, {b},{c},{d}")
# print(f"My husband name is: {a}")
# print(f"My name is: {b}")
# print(f"My first daughter name is: {c}")
# print(f"My second daughter name is: {d}")

# You must know of these brackets which are very much required in programming.

## "" - Double quotes
## '' - Single quotes
## () - Round brackets or Tuple bracket
## {} - Flower or Curly brackets
## [] - Square brackets
## <> - Angle brackets

a= input("Please enter the name that you wanted to display: ")
print(a)
b= input("Please enter the name that you wanted to display: ")
print(b)
c = input("Please enter the name that you wanted to display: ")
print(c)
d = input("Please enter the name that you wanted to display: ")
print(d)

print(f"My name is in Upper case: {a.upper()}")
print(f"My wife name is in Upper case: {b.upper()}")
print(f"my elder daughter name is in Upper case: {c.upper()}")
print(f"my little daughter name is in Upper case: {d.upper()}")

print(f"Sleeeping 2 seconds...")
time.sleep(2)
print(f"My name is in Lower case: {a.lower()}")
print(f"My wife name is in Lower case: {b.lower()}")
print(f"my elder daughter name is in Lower case: {c.lower()}")
print(f"my little daughter name is in Lower case: {d.lower()}")
print(f"Sleeeping 2 seconds...")
time.sleep(2)
print(f"Python list checking using student_list...")
student_list = ["tom","david","ed","john"]
for student in student_list:
    print(f"Top ranker in the class is: {student}")


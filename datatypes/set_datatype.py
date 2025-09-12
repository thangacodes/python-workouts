"""
Sets in Python are unordered collections. This means:
The order of items in a set is not guaranteed.
Every time you print a set, the order of elements may appear different.
Sets are also unique collections, so duplicate values are not allowed.
"""

import time as t 
orders = {"soap","shampoo","oil","comb","soap","oil"}
print(orders)
print(type(orders))
print(len(orders))
t.sleep(1)
numbers = { 1, 2, 3, 4, 5, 6, 7, 8, 9 , 6}
print(numbers)
print(type(numbers))
print(len(numbers))
t.sleep(1)
boolset = { True, False }
print(boolset)
print(type(boolset))
print(len(boolset))
t.sleep(1)
mixture = { 1, 2, 4, 6, "India", "America", "Google", True, False }
print(mixture)
print(type(mixture))
print(len(mixture))

"""
Note: In Python,

True is treated as the integer 1
False is treated as the integer 0
If we keep both 1 and True, but since they are considered equal (True == 1), only one of them is kept in the set.
Similarly, False is equivalent to 0, but since 0 isn't explicitly in your set, False is stored as-is.

"""



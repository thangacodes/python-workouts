"""
This program is to find out the given variables data type is tuple or not..
And if it sees the print type(variable) is class 'tuple', then prints as same
"""

import time as t 
teams = ("india", "pakistan","bangaladesh","srilanka","oman")
print(teams)
print(type(teams))
t.sleep(1)
teams_constuple = tuple(("India", "America", 5, 10, 15, True, False))
print(teams_constuple)
print(type(teams_constuple))
if isinstance(teams, tuple) and isinstance(teams_constuple, tuple):
  print(f"Both variables like teams and teams_constuple are tuple datatype")
else:
  print("It doesn't belong to any data type in python")

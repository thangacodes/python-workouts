### This is the page, where we can get custom function creation and examples for If conditional statements

# If conditional statements:
import time
a = input("Enter the day please:")
print(a)
print(f"the memory id of a is:{id(a)}")
time.sleep (2)
# If condition starts here.
if a == "monday":
  print("your assumed day is correct")
elif a != "monday":
  print("your assumption is totally wrong")
else:
  print("The Game is Over")

#### custom function creating
def printt():
    print("This is Python 3.2 Tutorial")
    print("This is Python 3.2 Tutorial")
    print("This is Python 3.2 Tutorial")
printt()

def evenOdd( x ):  
    if (x % 2 == 0):  
        print("even") 
    else:  
        print("odd") 
evenOdd(2)
evenOdd(3)

def student(firstname, lastname):   
     print(firstname, lastname)  
student(firstname='manivannan',lastname='murugan')
student(firstname='thangadurai',lastname='murugan')


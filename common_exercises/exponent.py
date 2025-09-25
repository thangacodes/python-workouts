import math
def exponent_func():
        
        a =input("Enter the number: ")
        b=input("Enter the power of exponents: ")
        print(f"You entered number is:{a}")
        print(f"Power of exponents is:{b}")
        result =math.pow(int(b),int(a))
        print(f"The exponent value of {a} is: {result}")
exponent_func()



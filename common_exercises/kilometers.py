import math
userinput=int(input("Enter the random kilometer in Integer:"))
print("Checking the entered km value is.upper(): ", userinput)
print("Checking the variable datatype is: ", type(userinput))
print("converting kilo meter into miles using math library")
km = 0.62137119
print("Checking 1km value is: ", km)
miles=(userinput * 0.62137119)
print(miles)

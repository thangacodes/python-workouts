import time, datetime

print("")
runtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Script runs at the time of: {runtime}")

userinput = input("Please enter the operation you would like to perform in Calculator (addition, subtraction, division): ").lower()
print(f"User entered operation is: {userinput}")
time.sleep(1)

def addition():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    z = a + b
    print(f"Addition of two numbers is: {z}")

def subtraction():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    z = a - b
    print(f"Subtraction of two numbers is: {z}")

def division():
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        z = a / b
        print(f"Division of two numbers is: {z}")

if userinput == "addition":
    print("Going to invoke addition function")
    addition()
elif userinput == "subtraction":
    print("Going to invoke subtraction function")
    subtraction()
elif userinput == "division":
    print("Going to invoke division function")
    division()
else:
    print("Please choose only operations like (addition, subtraction, division)")

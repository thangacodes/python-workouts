num1 = int(input("Enter a number pls:"))
print(num1)
num2 = float(input("Enter float number pls:"))
print(num2)
oper=input("Enter operator(+,-,*,/,^): ")
print(oper)
def calculate(num1,num2,oper):
    if oper == '+':
        result = num1 + num2
    elif oper == '-':
        result = num1 - num2
    elif oper == '*':
        result = num1 * num2
    elif oper == '/':
        result = num1 / num2
    elif oper == '^':
        result = num1 ** num2
    return result
result=calculate(num1,num2,oper)
print(result)

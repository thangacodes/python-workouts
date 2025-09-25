height = int(input("Enter your height in 'cm': "))
weight = int(input("Enter your weight in 'kg': "))
print("You've entered height as:", height)
print("You've entered weight as:", weight)
print("Converting height values from centimeter to meter begins....")
meter = height/100
print(meter)
print("Converted height value in meter is:", meter)
print("Calculating BMI using BMI formula...")
bmi = weight/meter ** 2
print("BMI value of yours is in float: ", bmi)
# print("BMI value of yours is in round off in int: ", round(bmi))
print (" ********** BMI REPORT TO THE USERS ********** ")
if bmi <= 18.5:
    print("You're Under Weight and body in your control...")
if bmi <= 24.9:
    print("Great! You're healthy and maintaining body correctly......")
elif bmi <= 29.9:
    print("You are overweight! Please take an action immediately....")
else:
    print("You are extra obesity!!!!....")

import time
print('*** User inputs validation on the district ***')
city_names = ["dharmapuri", "salem", "harur"]
userfeed = input("Please enter a city name: ")

if userfeed.isupper():
    print(f"The user entered city name is uppercase: {userfeed}")
    time.sleep(4)
    convert = userfeed.lower()
    print(f"After converting the city name into lowercase, the value of city name in lowercase is: {convert}")
    print(f"Checking {convert} value in stored variable called city_names")
    if convert in city_names:
        print("The user entered value exists in our database")
    else:
        print("The entered city does not exist in the city_names variable")
else:
    print(f"The user entered city name is in lowercase: {userfeed}")
    time.sleep(2)
    if userfeed in city_names:
        print(f"The entered city {userfeed} exists in the city_names variable")
    else:
        print(f"The entered city {userfeed} does not exist in the city_names variable")

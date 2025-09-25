import time
#Get the main string from the user
my_string = input("Please enter the string that you want to count: ")
print(f"User provided string is: {my_string}")
time.sleep(1)
total_count = len(my_string)
print(f"The total number of characters in the string is: {total_count}")

user_input = input("Do you want to play the quiz game? Say YES or NO: ")
print(f"You have entered the input value is: {user_input}")  ## In or when you use f-string, when you wanted to call variables, you should use like {variable_name}

## Conditional statement is starting here
if user_input == 'yes':  ## not qual !=
    print("You are good to play the quiz game...")
elif user_input == 'no':
    print("You are not eligible to play the game...")
    #print(f"You are not eligible to play the quiz game. Since you entered the user_input is {user_input}")
else:
    print(f"You have chosen the wrong user_input as {user_input}. Please try with the valid input...")

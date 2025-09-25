import time as t
x = "Python is a popular programming language. Python can be used on a server to create web applications"
userfeed = input("Please enter a keyword to check in the given statement: ").strip().lower()
print(f"User input is: {userfeed}")
t.sleep(2)

print(userfeed in x.lower())  # convert x to lower for case insensitive check
t.sleep(2)

print("Using if/else condition based")
if userfeed not in x.lower():
    print(f"'{userfeed}' does not exist in the given statement.")
elif userfeed in x.lower():
    print(f"'{userfeed}' exists in the given statement.")
else:
    print("You need to revisit the statement.")

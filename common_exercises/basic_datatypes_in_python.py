import time
import re
a="arn:aws:iam::123456789012:user/johndoe"
print("Converting a variable to upper case..")
print(a.upper())
b = "IndIA"
print("Converting a variable to lower case..")
c = print(b.lower())
time.sleep(2)
str1 = "Hello"
str2 = "World"
print("concatenation in progress..")
str3 = str1 + " " + str2
print(str3)
print("Using length function we will calculate how many characters of a string ")
d=len(b)
print("The length of the 'b' variable is:", d)
e=round(3.1456789, 3)
print("rounded value:", e)
text="The india is a good country"
pattern = r"india"
match = re.match(pattern, text)
if match:
    print("Match found:")
else:
    print("No match found")

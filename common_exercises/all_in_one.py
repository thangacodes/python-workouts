### Simple standard library function in Python ####

a = 'thangadurai'
b = 'eashwari'
c = 'vedhiksha shree'
print(a.upper())
print(b.upper())
print(c.upper())

#### Just importing math module to find out a number factorial
import math
a =5
print(math.factorial(a))
#### Just importing os module to create a sample document,excel,pdf,text file ####
#### Finally all the files will get deleted. In between we are using time module to take few seconds break each actions.

import os
import time
doc = open("C:/temp/sample.docx", "w")
doc.close()
time.sleep (3)
os.remove("C:/temp/sample.docx")
excel = open("C:/temp/sample.xlsx", "w")
excel.close()
time.sleep (3)
os.remove("C:/temp/sample.xlsx")
time.sleep (1)
pdf = open("C:/temp/sample.pdf", "w")
pdf.close()
time.sleep (3)
os.remove("C:/temp/sample.pdf")
time.sleep (1)
text = open("C:/temp/sample.txt", "w")
text.close()
time.sleep (3)
os.remove("C:/temp/sample.txt")
print(" After creating the files in the temp directory of the laptop. Then removed all the files like doc,xls,pdf,txt")

####Creating a simple custom function using
import time
def corona() :
    print("Corona is a covid-19")
    print("no Vaccine is still not found for it")
    print("Please wear mask on face")
    print (" Most common symptoms are fever,dry cough,tiredness")
time.sleep (2)
corona()  ## calling the custom function()

  


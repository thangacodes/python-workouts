import time
product_number="9670097688731"
type(product_number)
print("Given product value is as: ", product_number)
print("Sleeping for '2' seconds: ")
time.sleep(2)
ccode=product_number[0:3]
print("Length of country code is:", ccode)
pcode=product_number[3:8]
print("Length of product code is: ", pcode)
batnum=product_number[-5:]
print("Length of batch number is: ", batnum)
time.sleep(2)
print("Checking the required output values as below: ")
print("Country code: ", ccode)
print("Product code: ", pcode)
print("Batch number: ", batnum)

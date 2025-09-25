file1 = open('C:/temp/myfile.txt', 'w') 
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"] 
s = "Hello\n"
file1.write(s)
file1.writelines(L) 
file1.close() 
file1 = open('C:/temp/myfile.txt', 'r') 
print(file1.read()) 
file1.close() 

def dob_finding():
    import time
    month_name =["January","February","March","April","May","June","July","August","September","October","November","December"]
    print (month_name)
    y=len(month_name)
    y
    print("The length of the list is:",y)
    print("Taking '5' seconds deep break......")
    time.sleep(5)
    dob =input("Please enter your date of birth: ", )
    dob
    print("You have entered the dob date is:", dob)
    month_value  = int(dob.split('/')[1])
    print("your birth month in number is:", month_value )
    print("Your born in the month of:", (month_name[month_value -1]))
dob_finding()

## Takeaway is, using split function, we can split dob date into '/' and then we can use that split variable in the last. If we use minus of date of split, it fullfil our requirements..

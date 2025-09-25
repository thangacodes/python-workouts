## Finding number days in a month using Python Script ############

days = ("Number of days in any months of an year are 28, 29, 30, 31")
print(days) # To double check
days=input("Enter the no of days:")
if days == '28' or days== '29':
    print("February")  
elif days == '31':
    print("January, March, May, July, August, October, December")
elif days == '30':
  print("April, June, September, November")
else:
  print ("Invalid Entry")
  
 ################# Finding how many tuesday comes in any month any year in the calendar ##############
import calendar
import time
mydays = {'mon':0, 'tue':1, 'wed':2, 'thu':3, 'fri':4, 'sat':5, 'sun':6}
print(mydays)
time.sleep (2)

year = int(input("Enter year number : "))
month = int(input("Enter month number : "))
str_day = input("Choose any day mon,tue,wed,thu,fri,sat,sun : ")

print(calendar.monthcalendar(year,month))      # using calendar module to get month information

day = mydays[str_day]
for i in calendar.monthcalendar(year,month):
     if i[day] != 0:
          print(f"{str_day} lies on {i[day]}/{month}/{year}")

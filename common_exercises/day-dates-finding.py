## This is the page, where you can get to know about the day with the dates.

print("To find out the correct day with dates using python")
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
          print(f"{str_day} falls on {i[day]}/{month}/{year}")

##################################################################

## this is to find out no of days in any months of any year previous or feature year.

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
 
import datetime
import time
days_of_week = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
print(days_of_week) # To double check
for i in days_of_week:
  print(i)


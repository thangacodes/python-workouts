import time
print("Iterating weekdays in Python...")
weekdays=["monday","tuesday","wednesday","thursday","friday"]
for w in weekdays:
    print(w)
time.sleep(2)
print("If the weekday is Thursday, print only when it is on the above weekday list!..")
weekdays=["monday","tuesday","wednesday","thursday","friday"]
for w in weekdays:
    if w == "thursday":
        print(w)
time.sleep(2)
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
for w in weekdays:
    print(w)
    if w == "thursday":
        break

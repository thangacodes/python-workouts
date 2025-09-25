import time 
print("Identifying only weekend days from the given list...")
weekends=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
for w in weekends:
    print(w)
time.sleep(2)
print("Weekends can only be detected by Python Scripts...")
weekends=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
for w in weekends:
    if w == "saturday" or w == "sunday":
        print(w)


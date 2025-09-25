####### This is the If-else conditional check python Script  ######

city = input("Please enter your city: ").lower()

if city == "chennai":
    print("Wow! You are living in the capital of Tamil Nadu.")
    area_name = input("Enter your area name in the city: ").lower()
    if area_name == "velacheri":
        print("Awesome, you are living near OMR highway.")
elif city == "ooty":
    print("Oh! You are living in a tourist city.")
    area_name = input("Enter your area name in the city: ").lower()
    if area_name == "tirpur":  # Confirm if this is the intended area name in Ooty
        print("Awesome, you are living near the loom manufacturing area.")
elif city == "namakkal":
    print("Marvellous! You are living in a clean city.")
    area_name = input("Enter your area name in the city: ").lower()
    if area_name == "salem road":
        print("Awesome, you are living near the road to TKcode.")
else:
    print("The city name you entered is not in our database.")


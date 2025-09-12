student_dict ={
    "name": "thangadurai",
    "age": 30,
    "hobbies": ["cricket","tennis"]
}
key_value = input("Enter the key to retrieve: ").lower()
result = student_dict.get(key_value, "No Key Found")
print(f"Value of key is {key_value} is {result}")

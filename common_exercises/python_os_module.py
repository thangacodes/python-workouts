import os
import socket
import time
print("Python script to talk to capture OS related module stuff and networking")
print("\n")
# Get the current working directory
current_directory = os.getcwd()
# Print the current working directory
print("You are currently working on directory:", current_directory)
# Get the user id who logged in
user_id=os.getuid()
print("Your id is:", user_id )
# Get the user environment variable for HOME
env_vars=os.getenv(("HOME"))
print(f"User variable: {env_vars}")
# Get the user who logged into the box
logged_in = os.getlogin()
print(f"The user who logged into the box is: {logged_in}")
# Create the "india" folder
india_dir = f"{current_directory}/india"
try:
    # Ask for user input
    user_input = input("Do you want to create the folder (say yes or no): ").strip().lower()
    # Check if user input is "yes"
    if user_input == "yes":
        print("You are good to create the directory")
        os.mkdir(india_dir)
        print(f"Created folder: {india_dir}")
    else:
        print("Folder creation aborted.")   
except FileExistsError:
    print(f"Folder '{india_dir}' already exists.")
except Exception as e:
    print(f"Error creating folder: {e}")
time.sleep(2)
hostname = socket.gethostname()
print(f"My lap hostname is: {hostname}")
mylap_ip = socket.gethostbyname(hostname)
print(f"My lap ip address is: {mylap_ip}")
google_ip= socket.gethostbyname('google.com')
print(f"Here's the google ip: {google_ip}")
chatgpt_ip = socket.gethostbyname('chatgpt.com')
print(f"Here's the chatgpt ip address: {chatgpt_ip}")

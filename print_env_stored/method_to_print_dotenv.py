"""
Script Title: Loading and Accessing Environment Variables Using python-dotenv

This script demonstrates three different methods to load environment variables
from a `.env` file and access their values in Python using the `dotenv` library.

Make sure you have a `.env` file with keys like:
access_key=your_access_key_here
secret_key=your_secret_key_here
"""

import os, time
from dotenv import load_dotenv

# Load .env file once at the start
load_dotenv()

# Method 1: Direct access after loading
print("\nMethod 1: Direct access after loading\n")
access_key = os.getenv("access_key")
secret_key = os.getenv("secret_key")

print(f"Access Key: {access_key}")
print(f"Secret Key: {secret_key}")
time.sleep(2)

# Method 2: Encapsulated in a function that prints the values
print("\nMethod 2: Function that loads and prints the environment variables\n")

def load_and_print_env():
    # No need to load_dotenv() again since it's loaded at start
    access_key = os.getenv("access_key")
    secret_key = os.getenv("secret_key")

    print(f"Access Key: {access_key}")
    print(f"Secret Key: {secret_key}")

load_and_print_env()
time.sleep(2)

# Method 3: Function that returns the values, then print outside
print("\nMethod 3: Function that returns the environment variables\n")

def get_env_values():
    # Again, no need to call load_dotenv() again here
    access_key = os.getenv("access_key")
    secret_key = os.getenv("secret_key")
    return access_key, secret_key

access_key, secret_key = get_env_values()
print(f"Access Key: {access_key}")
print(f"Secret Key: {secret_key}")

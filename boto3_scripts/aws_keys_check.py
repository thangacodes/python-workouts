import os, time
from configparser import ConfigParser

def read_aws_credentials(profile='default'):
    # Path to AWS credentials file
    credentials_path = os.path.expanduser('~/.aws/credentials')

    # Create a ConfigParser object
    config = ConfigParser()

    # Read the file
    config.read(credentials_path)

    # Check if profile exists
    if profile not in config:
        print(f"Profile '{profile}' not found in {credentials_path}")
        return None, None

    # Extract keys
    access_key = config[profile].get('aws_access_key_id')
    secret_key = config[profile].get('aws_secret_access_key')

    return access_key, secret_key

# Usage
access_key, secret_key = read_aws_credentials()

print(f"AWS access_key: {access_key}")
print(f"AWS secret_key: {secret_key}")

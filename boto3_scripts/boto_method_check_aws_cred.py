import boto3
from botocore.exceptions import ProfileNotFound

def read_aws_credentials(profile='default'):
    try:
      # Create a session using the specified profile
      session = boto3.Session(profile_name=profile)
        
      # Get credentials from the session
      credentials = session.get_credentials()
        
      # Credentials can be None if the profile is not set up properly
      if credentials is None:
        print(f"No credentials found on profile: {profile}")
        return None, None
        
      # Access key and secret key
      access_key = credentials.access_key
      secret_key = credentials.secret_key
      return access_key, secret_key
        
    except ProfileNotFound:
      print(f"Profile '{profile}' not found.")
      return None, None

# Usage
access_key, secret_key = read_aws_credentials()
print(f"Printing the available AWS access & secret key values..")
print("")
print(f"AWS access_key: {access_key}")
print(f"AWS secret_key: {secret_key}")

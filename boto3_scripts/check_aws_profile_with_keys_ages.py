"""
Script to check whether required AWS profiles (primary, secondary) exist,
and display the access key age, including how many days past the rotation threshold.
"""

import boto3
import datetime
import time
import sys
import os
from configparser import ConfigParser
from botocore.exceptions import ClientError, ProfileNotFound

# --- Configuration ---
CREDENTIALS_PATH = "/home/ec2-user/.aws/credentials"
PROFILES_TO_CHECK = ['dev', 'prod']
ROTATION_THRESHOLD_DAYS = 30
IAM_USERNAME = 'captain'

# --- Execution Start ---
exec_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"The script is executed at: {exec_time}")

print(f"Checking AWS credentials file at: {CREDENTIALS_PATH}")
if not os.path.exists(CREDENTIALS_PATH):
    print(f"Credentials file not found at {CREDENTIALS_PATH}")
    sys.exit(1)

# --- Read credentials ---
config = ConfigParser()
config.read(CREDENTIALS_PATH)

print("\n--------------------------------------------------")

for profile in PROFILES_TO_CHECK:
    if profile in config:
        print(f"[{profile}] profile found in credentials file.")
        aws_access_key = config[profile].get('aws_access_key_id')
        aws_secret_key = config[profile].get('aws_secret_access_key')
        print(f"{profile} access_key : {aws_access_key}")
        print(f"{profile} secret_key : {aws_secret_key}")

        try:
            # Create session and IAM client
            session = boto3.Session(profile_name=profile)
            iam_client = session.client('iam')

            # Use hardcoded username
            print(f"Checking access keys for IAM user: {IAM_USERNAME}")
            keys = iam_client.list_access_keys(UserName=IAM_USERNAME)['AccessKeyMetadata']

            if not keys:
                print(f"No access keys found for user {IAM_USERNAME}")
                continue

            for key in keys:
                key_id = key['AccessKeyId']
                create_date = key['CreateDate']
                age_days = (datetime.datetime.now(datetime.timezone.utc) - create_date).days

                print(f"Access Key ID : {key_id}")
                print(f"Created On    : {create_date.strftime('%Y-%m-%d')}")
                print(f"Age           : {age_days} days")

                if age_days <= ROTATION_THRESHOLD_DAYS:
                    print(f"Access key is just created (≤ {ROTATION_THRESHOLD_DAYS} days). No rotation needed.")
                else:
                    days_over = age_days - ROTATION_THRESHOLD_DAYS
                    print(f"Access key is older than {ROTATION_THRESHOLD_DAYS} days"
                        f"(by {days_over} days). Rotation recommended!")

        except ProfileNotFound:
            print(f"Profile [{profile}] not found in AWS config.")
        except ClientError as error:
            print(f"Error fetching IAM info for profile [{profile}]: {error}")
    else:
        print(f"[{profile}] profile not found in credentials file.")
print("-----------------------------------------------------------------")

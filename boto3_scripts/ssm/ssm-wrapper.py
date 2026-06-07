#!/usr/bin/env python3

import boto3
import subprocess
import sys
import configparser
import os
from pathlib import Path

print("=" * 85)
print("Script is to connect the running machine in aws account using ssm over ssh method")
print("=" * 85)

REGIONS = [
    "ap-south-1",
    "ap-south-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "eu-west-2",
    "eu-west-3",
]

def parse_args():
    args = sys.argv[1:]

    if not args:
        print("Usage: ssm <instance-id | instance-name> [--verbose]")
        sys.exit(1)

    target = None
    verbose = False

    for arg in args:
        if arg == "--verbose":
            verbose = True
        else:
            target = arg

    return target, verbose

def get_sessions(verbose=False):
    credentials_file = Path.home() / ".aws" / "credentials"

    if not credentials_file.exists():
        raise Exception(f"Credentials file not found: {credentials_file}")

    config = configparser.ConfigParser()
    config.read(credentials_file)

    profiles = config.sections()

    if verbose:
        print("")
        print("[INFO] Scanning AWS credential profiles...")
        for profile in profiles:
            print(f"[INFO] Found profile: {profile}")

    if not profiles:
        raise Exception("No AWS profiles found")

    sessions = []

    for profile in profiles:
        try:
            session = boto3.Session(profile_name=profile)
            sessions.append((session, profile))

        except Exception as e:
            if verbose:
                print(
                    f"[WARN] Unable to create session "
                    f"for profile {profile}: {e}"
                )

    if not sessions:
        raise Exception("No valid AWS sessions could be created")

    return sessions


def get_profile_credentials(profile):

    credentials_file = Path.home() / ".aws" / "credentials"

    config = configparser.ConfigParser()
    config.read(credentials_file)

    access_key = config[profile]["aws_access_key_id"]
    secret_key = config[profile]["aws_secret_access_key"]
    session_token = config[profile].get("aws_session_token")

    return access_key, secret_key, session_token


def find_instance(session, target, verbose=False):

    is_instance_id = target.startswith("i-")

    if verbose:
        print(f"[INFO] Looking for: {target}")
        print(f"[INFO] Scanning regions: {', '.join(REGIONS)}")

    for region in REGIONS:

        if verbose:
            print(f"[INFO] Scanning region: {region}")

        try:

            ec2 = session.client("ec2", region_name=region)

            if is_instance_id:

                response = ec2.describe_instances(
                    InstanceIds=[target]
                )

            else:

                response = ec2.describe_instances(
                    Filters=[
                        {
                            "Name": "tag:Name",
                            "Values": [target]
                        },
                        {
                            "Name": "instance-state-name",
                            "Values": ["running"]
                        }
                    ]
                )

            for reservation in response["Reservations"]:
                for instance in reservation["Instances"]:

                    instance_id = instance["InstanceId"]

                    name = ""

                    for tag in instance.get("Tags", []):
                        if tag["Key"] == "Name":
                            name = tag["Value"]
                            break

                    if verbose:
                        print(
                            f"[INFO] Found instance "
                            f"(Name={name}, InstanceId={instance_id}) "
                            f"in region {region}"
                        )

                    return instance_id, name, region

        except Exception as e:

            if verbose:
                print(
                    f"[DEBUG] Region {region} did not match "
                    f"or returned error: {e}"
                )

    return None, None, None


def start_ssm(instance_id, region, profile, verbose=False):

    access_key, secret_key, session_token = \
        get_profile_credentials(profile)

    env = os.environ.copy()
    env["AWS_ACCESS_KEY_ID"] = access_key
    env["AWS_SECRET_ACCESS_KEY"] = secret_key

    if session_token:
        env["AWS_SESSION_TOKEN"] = session_token

    if verbose:
        print(f"[INFO] Exporting AWS credentials for profile: {profile}")
        print("[INFO] Starting SSM session...")

    subprocess.run(
        [
            "aws",
            "ssm",
            "start-session",
            "--target",
            instance_id,
            "--region",
            region,
        ],
        env=env,
    )


def main():

    target, verbose = parse_args()

    try:
        sessions = get_sessions(verbose)

    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    for session, profile in sessions:

        try:
            sts = session.client("sts")
            identity = sts.get_caller_identity()

            if verbose:
                print("")
                print(
                    f"[INFO] Searching profile={profile}"
                )
                print(
                    f"[INFO] AWS Identity: {identity['Arn']}"
                )

        except Exception as e:

            if verbose:
                print(
                    f"[WARN] Failed to validate "
                    f"profile {profile}: {e}"
                )

            continue
        instance_id, instance_name, region = find_instance(
            session,
            target,
            verbose
        )

        if instance_id:
            print()
            print("MACHINE INFORMATION:")
            print("")
            print(f"Profile        : {profile}")
            print(f"Instance Name  : {instance_name}")
            print(f"Found instance : {instance_id}")
            print(f"Region         : {region}")
            print()
            print(f"==> Connecting to {instance_id} via SSM...")

            start_ssm(
                instance_id,
                region,
                profile,
                verbose
            )
            return
    print("Instance not found in any AWS profile")
    sys.exit(1)
if __name__ == "__main__":
    main()

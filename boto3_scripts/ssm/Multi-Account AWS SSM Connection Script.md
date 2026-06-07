## Multi-Account AWS SSM Connection Script:

This script has been enhanced to support **multiple AWS accounts (profiles)** defined in `~/.aws/credentials`.

### Key Improvements:

- Automatically detects all AWS profiles (e.g., dev, stage, preprod, prod)
- Searches across **all configured AWS regions**
- Finds EC2 instances across multiple AWS accounts without manually switching profiles
- Automatically selects the correct AWS profile for SSM connection
- Simplifies cross-account instance access using a single command

### How It Works:

1. Loads all profiles from `~/.aws/credentials`
2. Iterates through each AWS account profile
3. Scans all predefined AWS regions
4. Matches the EC2 instance by:
   - Instance ID OR
   - EC2 Name tag
5. Initiates SSM session using the matching account automatically

### Usage:

```bash
ssm <instance-id | instance-name> [--verbose]

root@INB-512693:~# ssm i-0fdb320b341ce11c1 --verbose
=====================================================================================
Script is to connect the running machine in aws account using ssm over ssh method
=====================================================================================

[INFO] Scanning AWS credential profiles...
[INFO] Found profile: joes

[INFO] Searching profile=captain
[INFO] AWS Identity: arn:aws:iam::500048406020:user/joes
[INFO] Looking for: i-0fdb320b341ce11c1
[INFO] Scanning regions: ap-south-1, ap-south-2, ap-southeast-1, ap-southeast-2, us-east-1, us-east-2, us-west-1, eu-west-2, eu-west-3
[INFO] Scanning region: ap-south-1
[INFO] Found instance (Name=crosschecking, InstanceId=i-0fcb320b246ce98c6) in region ap-south-1

MACHINE INFORMATION:

Profile        : captain
Instance Name  : crosschecking
Found instance : i-0fdb320b341ce11c1
Region         : ap-south-1

==> Connecting to i-0fdb320b341ce11c1 via SSM...
[INFO] Exporting AWS credentials for profile: captain
[INFO] Starting SSM session...

Starting session with SessionId: joes-vigcb2r955ygz8d5gspdkhragu
sh-5.2$ hostname
ip-172-31-45-248.ap-south-1.compute.internal

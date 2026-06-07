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

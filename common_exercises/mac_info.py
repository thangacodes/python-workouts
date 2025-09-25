import os
import time
import datetime

run_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(f"script runs at: {run_time}")

print("Your system hostname is:")
os.system('hostname')

os.system('system_profiler SPHardwareDataType | grep "Serial Number"')

print("Your system ip address is:")
os.system("ifconfig en0 | grep 'inet ' | awk '{print $2}'")

print("Your login name is:")
os.system('whoami')

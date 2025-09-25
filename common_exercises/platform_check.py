import datetime
import time
import platform
script_exec_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Script runs at: {script_exec_time}")
time.sleep(1)
print("=========================================================")
# List of server names
servers = ["host1", "host2"]

# Function to print server name
def print_server(server):
    print(f"Starting with the host: {server}")
    mac_version = platform.mac_ver()[0]
    print("macOS Version:", mac_version)
# Using map to iterate and apply the function
list(map(print_server, servers))
time.sleep(5)
print("========================================")
print("Your Operating System:", platform.system())
print("Your OS Version name:", platform.version())
print("Your Machine name:", platform.machine())
print("Your Processor name:", platform.processor())

import datetime
import time

script_exec_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Script runs at: {script_exec_time}")
time.sleep(1)
print("=========================================================")
# List of server names
servers = ["host1", "host2", "host3", "host4", "host5", 
           "host6", "host7", "host8", "host9", "host10"]
# Function to print server name
def print_server(server):
    print(f"Starting with the host: {server}")
# Using map to iterate and apply the function
list(map(print_server, servers))

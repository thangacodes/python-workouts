## This page is to show us, how to check the ping response from the client machines using Python Script.
import os
import time
iplist = ["1.1.1.1", "49.207.206.230", "192.168.0.134"]
for ip in iplist:  ### For loop using
    response = os.popen(f"ping {ip}").read()
    if "received = 8" in response:
        print(f"UP {ip} and ping successfull")
    else:
        print(f"DOWN {ip} and ping unsuccessfull")
time.sleep(1)
print ("Script is executed and exited")

## This is the page, where you write up a script to find out if you want to know any particular windows service running or not

First and formost, we need to get installed windows python package
# https://pypi.org/project/psutil/
To install pip libraries, use the following method:
  a) Open CMD or Windows PowerShell with Admin previlege,
  b) pip install psutil
  c) pip list ## It will list out the pip libraries that got installed on the laptop.

Note: 
psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. 
It is useful mainly for system monitoring, profiling and limiting process resources and management of running processes.
It implements many functionalities offered by classic UNIX command line tools such as ps, top, iotop, lsof, netstat, ifconfig, free and others. 
psutil currently supports the following platforms:

Linux
Windows
macOS
FreeBSD, OpenBSD, NetBSD
Sun Solaris
AIX
Supported Python versions are 2.6, 2.7, 3.4+ and PyPy.
======================================================================
## Note: Here, we are checking Jenkins service status on windows OS. You can modify as per your wish to check any windows services,
# Spooler,Dhcp,Netlogon,Dnscache,Jenkins,LanmanWorkstation and so on...

import psutil
import time
f = open("C:/Users/SG0307269/Desktop/Python-Scripts/host.txt", "r")
if f.mode == "r":
    contents =f.read()
    print(f"The file contain server name is:{contents}")
time.sleep(1)

time.sleep(2)
def get_service(Jenkins): # custom function
    service = Jenkins
    try:
        service = psutil.win_service_get(Jenkins)
        service = service.as_dict()
    except Exception as ex:
        # raise psutil.NoSuchProcess if no service with such name exists
        print(str(ex))

    return service

service = get_service('Jenkins')

if service:
    print("Service found: ", service)
else:
    print("Service not found")

if service and service['status'] == 'running':
    print("Service is running")
else: 
    print("Service is not running")
    
##### Note: 

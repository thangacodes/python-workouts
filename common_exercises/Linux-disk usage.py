## This repo will show you, how to find out disk usage in any of Linux flavours using Python script,

## Importing OS module
import os                                                                                                                                                                     
du = os.popen("df -h").readlines()   
from pprint import pprint
pprint(du)

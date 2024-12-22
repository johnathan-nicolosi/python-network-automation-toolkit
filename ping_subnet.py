######################################################
#     This script only works on Windows machines     #
######################################################

import platform
import subprocess

# Define the subnet
subnet = "192.168.2." # verify your subnet using the ipconfig command  in Command Prompt

# Detect the OS and set ping parameters
param = "-n" if platform.system().lower() == "windows" else "-c"
search_string = b"TTL" if platform.system().lower() == "windows" else b"64 bytes"

# Iterate through the last octet of the subnet
for i in range(1, 255):
    ip = subnet + str(i)
    result = subprocess.run(['ping', param, '1', ip], stdout=subprocess.PIPE)
    
    # Check if the output indicates the host is reachable
    if search_string in result.stdout:
        print(f'{ip} is up')
    else:
        print(f'{ip} is down')

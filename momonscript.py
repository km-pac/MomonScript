# import pexpect
import os
from colorama import Fore, Style, init

# # CLEANING THE FIRST FILE FROM TWMON SHEET
with open('twmon.txt', 'r') as file1:
  cleaned_iplist_twmon = []
  iplist = file1.readlines()  
  for line in iplist:
      rem_ip = line.upper().replace("SUBNET", '').replace('NO NEW IP', '').replace('\n', '')
      if rem_ip != '':
          cleaned_iplist_twmon.append(rem_ip)

# # CLEANING THE FIRST FILE FROM MOMON SHEET
with open('momon.txt', 'r') as file2:
    cleaned_iplist_momon = []
    dataline = file2.read()
    iplist = dataline.replace('[','').replace(']','').replace('"','').replace('\\','').split(",")
    cleaned_iplist_momon = [ip for ip in iplist if "/" in ip]

# # CLOSE BOTH FILES
file1.close()
file2.close()

# # FOR DEBUGGING
# # print(cleaned_iplist_twmon)
# # print(cleaned_iplist_momon)
# # print("TWMON")
# # for line in cleaned_iplist_twmon:
# #   print(line)
# # print("\n\n\nMOMON")
# # for line in cleaned_iplist_momon:
# #   print(line)

new_ips = [element for element in cleaned_iplist_momon if element not in cleaned_iplist_twmon]


print("NEW IP ADDRESSES")

for line in new_ips:
    modified_ip = line.split('.0/')[0] + '.2'
    ping_response = os.system("fping -c 1 -r 0 {}".format(modified_ip) + " > /dev/null 2>&1")

    if ping_response == 0:
        print(Fore.GREEN + "\n{} is up!".format(modified_ip) + Fore.WHITE)
        traceroute_response = os.system("traceroute -I {}".format(modified_ip) + " > /dev/null 2>&1")

        # Run the traceroute command and capture the output
        traceroute_output = subprocess.check_output(traceroute_response, shell=True, stderr=subprocess.DEVNULL, text=True)
        
        # Split the output into lines and extract the second-to-last line
        traceroute_lines = traceroute_output.split('\n')
        second_to_last_output = traceroute_lines[-2]

    else:
        print("{} is down!".format(modified_ip))

 

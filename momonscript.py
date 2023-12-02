# import pexpect
import os
import subprocess
import json 
from urllib.request import urlopen 
from colorama import Fore, Style, init

os.system("clear")

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

new_ips = [element for element in cleaned_iplist_momon if element not in cleaned_iplist_twmon]

print("NEW IP ADDRESSES")

for line in new_ips:
    modified_ip = line.split('.0/')[0] + '.2'
    ping_response = os.system("fping -c 1 -r 0 {}".format(modified_ip) + " > /dev/null 2>&1")

    if ping_response == 0:
        print(Fore.GREEN + "\n{} is up!".format(modified_ip) + Fore.WHITE)
    
        output = subprocess.check_output("traceroute -I {}".format(modified_ip), shell=True).decode("utf-8").strip("\n ' '")
        output_lines = output.splitlines()

        hop_list = []
        for line in output_lines:
            try: 
              extracted_hop = line.split("(")[1].split(")")[0]
              # print("HOP: " + extracted_hop)
              hop_list.append(extracted_hop)
            except: continue
        print(Fore.GREEN + "LAST HOP: " + hop_list[len(hop_list)-3] + Fore.WHITE + "\n")
    else:
        print("{} is down!".format(modified_ip))

 

# import pexpect
import os, subprocess, json
from urllib.request import urlopen 
from colorama import Fore, Style, init

os.system("clear")
twmon_file = "twmon.txt"
momon_file = "momon.txt"

# CLEANING THE FIRST FILE FROM TWMON SHEET
def extract_twmon_ip(file):
  with open('twmon.txt', 'r') as file1:
    cleaned_iplist_twmon = []
    iplist = file1.readlines()  
    for line in iplist:
        rem_ip = line.upper().replace("SUBNET", '').replace('NO NEW IP', '').replace('\n', '')
        if rem_ip != '':
            cleaned_iplist_twmon.append(rem_ip)
  file1.close()
  return cleaned_iplist_twmon

# CLEANING THE FIRST FILE FROM MOMON SHEET
def extract_momon_ip(file):
  with open('momon.txt', 'r') as file2:
      cleaned_iplist_momon = []
      dataline = file2.read()
      iplist = dataline.replace('[','').replace(']','').replace('"','').replace('\\','').split(",")
      cleaned_iplist_momon = [ip for ip in iplist if "/" in ip]
  file2.close()
  return cleaned_iplist_momon

cleaned_iplist_twmon = extract_twmon_ip(twmon_file)
cleaned_iplist_momon = extract_momon_ip(momon_file)

# COMPARING TWMON AND MOMON FILE
new_ips = [element for element in cleaned_iplist_momon if element not in cleaned_iplist_twmon]

print(Fore.CYAN + "IP ADDRESSES FOUND ON MOMON THAT ARE NOT IN TWMON\n" + Fore.WHITE)

hop_list = []
verified_hop_list = []
verified_network_list = []
isp_list = []

# PINGING + TRACEROUTING THE NEW NETWORK 
for line in new_ips:
    modified_ip = line.split('.0/')[0] + '.2'
    ping_response = os.system("fping -c 1 -r 0 {}".format(modified_ip) + " > /dev/null 2>&1")
    
    if ping_response == 0:
        print(Fore.GREEN + "\n{} is up!".format(modified_ip) + Fore.WHITE)
        verified_network_list.append(line)
        output = subprocess.check_output("traceroute -I {}".format(modified_ip), shell=True).decode("utf-8").strip("\n ' '")
        output_lines = output.splitlines()
        print("Performing traceroute on " + modified_ip)
        for line in output_lines:
          try: 
            extracted_hop = line.split("(")[1].split(")")[0]
            hop_list.append(extracted_hop)
          except: continue
            
        final_hop = hop_list[len(hop_list)-3]
        print(Fore.GREEN + "LAST HOP: " + final_hop + Fore.WHITE + "\n")
        verified_hop_list.append(final_hop)
      
    else:
        print("{} is down!".format(modified_ip))

# EXTRACTING THE ISP OF THE LAST HOP
for hop in verified_hop_list:
    isp_trace_url = "https://ipapi.co/{}/json".format(hop)
    bak_isp_trace_url = "http://ip-api.com/json/{}".format(hop)
    
    response = urlopen(isp_trace_url)
    data_json = json.loads(response.read())

    bak_response = urlopen(bak_isp_trace_url)
    bak_data_json = json.loads(bak_response.read())
    print(bak_data_json)

    if 'org' in data_json and data_json['org'] is not None:
      isp_list.append(data_json['org'])
    elif 'isp' in bak_data_json:
      isp_list.append(bak_data_json['isp'])
   
# print(type(isp_list[0]))

# CONDITIONAL: IF THERE ARE NEW ENTRY FOR TWMON
if verified_network_list != []:
  print(Fore.CYAN + "\nNEW ENTRIES FOR TWMON\n" + Fore.WHITE)
  for index, entry in enumerate(verified_network_list):
    print(Fore.CYAN + verified_network_list[index])
    print(Fore.GREEN + "LAST HOP: " + verified_hop_list[index])
    try:
      print(Fore.GREEN + "ISP: " + isp_list[index] + "\n" + Fore.WHITE)
    except: continue
else: print(Fore.CYAN + "\nNO NEW ENTRIES FOR TWMON\n" + Fore.WHITE)
 

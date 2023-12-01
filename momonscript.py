import pexpect

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
ping_count = 1
for line in new_ips:
    print(line)
    modified_ip = line.split('.0/')[0] + '.2'
    ping_command = "ping -c {} {}".format(ping_count, modified_ip)
    ping_result = pexpect.spawn(ping_command)
    ping_result.expect(pexpect.EOF)

    # Check if the ping result contains the expected response
    if "{} packets transmitted, {} received".format(ping_count, ping_count) in ping_result.before.decode("utf-8"):
        print("{} is pingable".format(modified_ip))
    else:
        print("{} is not pingable".format(modified_ip))

 


# child = pexpect.spawn('ping -c 5 ', new_ips[0])

# while 1:
#         line = child.readline()
#         if not line: break
#         print line,

# CLEANING THE FIRST FILE FROM TWMON SHEET
with open('twmon.txt', 'r') as file1:
  cleaned_iplist_twmon = []
  iplist = file1.readlines()  
  for line in iplist:
      rem_ip = line.upper().replace('NO NEW IP', '').replace('\n', '')
      if rem_ip != '':
          cleaned_iplist_twmon.append(rem_ip)

  
with open('momon.txt', 'r') as file2:
    cleaned_iplist_momon = []
    dataline = file2.read()
    iplist = dataline.replace('[','').replace(']','').replace('"','').replace('\\','').split(",")
    cleaned_iplist_momon = [ip for ip in iplist if "/" in ip]

file1.close()
file2.close()

# print(cleaned_iplist_twmon)
# print(cleaned_iplist_momon)

# print("TWMON")
# for line in cleaned_iplist_twmon:
#   print(line)
# print("\n\n\nMOMON")
# for line in cleaned_iplist_momon:
#   print(line)

new_ips = [element for element in cleaned_iplist_momon if element not in cleaned_iplist_twmon]

print("NEW IP ADDRESSES")'
count = 1
for line in new_ips:
  print(count + " " + line)
  count++



# CLEANING THE FIRST FILE FROM TWMON SHEET
with open('file1.txt', 'r') as file1:
  a_iplist = []
  cleaned_iplist = []
  iplist = file1.readlines()
  for line in iplist:
    rem_ip = line.replace('No new IP', '')
    rem_space = rem_ip.replace('\n', '')
    a_iplist.append(rem_space)
    if rem_space != '':
        cleaned_iplist.append(rem_space)

  # for ip in a_iplist:
  #   if ip != '':
  #     cleaned_iplist.append(ip)

  for ip in cleaned_iplist:
    print(ip + "\n")




  
 
# with open('file1.txt', 'w') as file1:
#     file1.write(rem_dob)

file1.close()


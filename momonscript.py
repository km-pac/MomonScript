# CLEANING THE FIRST FILE FROM TWMON
with open('file1.txt', 'r') as file1:
  # filedata = file1.read()
  # rem_ip = filedata.replace('No new IP', '')
  # # rem_space = rem_ip.replace('\n', ' ')
  # # rem
  a_iplist = []
  iplist = file1.readlines()
  for line in iplist:
    rem_ip = line.replace('No new IP', '')
    rem_space = rem_ip.replace('\n', '')
    if line != " ":
      a_iplist.append(rem_space)
    
  
  print(a_iplist)
  
 
# with open('file1.txt', 'w') as file1:
#     file1.write(rem_dob)

file1.close()


# CLEANING THE FIRST FILE FROM TWMON
with open('file1.txt', 'r') as file1:
  filedata = file1.read()
  rem_ip = filedata.replace('No new IP', '')
  # rem_space = rem_ip.replace('\n', ' ')
  # rem

  a_ipadd = []
  a_ipaad.append(rem_ip)
  print(a_ipadd)
  
 
with open('file1.txt', 'w') as file1:
    file1.write(rem_dob)

file1.close()


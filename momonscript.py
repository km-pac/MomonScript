# CLEANING THE FIRST FILE FROM TWMON
with open('file1.txt', 'r') as file1:
  filedata = file1.read()
  rem_ip = filedata.replace('No new IP', '')

  lines = file1.readlines()
  for line in lines:
    rem_space = rem_ip.replace(' ','')

with open('file1.txt', 'w') as file1:
  file1.write(rem_space)

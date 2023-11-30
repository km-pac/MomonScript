# CLEANING THE FIRST FILE FROM TWMON
with open('file1.txt', 'r') as file1:
  filedata = file1.read()
  rem_ip = filedata.replace('No new IP', '')
  rem_space = rem_ip.replace(' ', '\r')

with open('file1.txt', 'w') as file1:
  file1.write(rem_space)

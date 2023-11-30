# CLEANING THE FIRST FILE FROM TWMON
# Read in the file
with open('file1.txt', 'r') as file1:
  filedata = file1.read()

# Replace the target string
rem_ip = filedata.replace('No new IP', '')
rem_space = rem_ip.replace('.', '|')

# Write the file out again
with open('file1.txt', 'w') as file1:
  file1.write(rem_space)

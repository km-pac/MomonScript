# CLEANING THE FIRST FILE FROM TWMON
# Read in the file
with open('text1.txt', 'r') as text1:
  filedata = text1.read()

# Replace the target string
filedata1 = filedata.replace('No new IP', '')
filedata2 = filedata.replace('\n', '\r')

# Write the file out again
with open('file.txt', 'w') as file:
  file.write(filedata1)
  file.write(filedata2)

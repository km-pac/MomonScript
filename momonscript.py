# CLEANING THE FIRST FILE FROM TWMON SHEET
with open('file1.txt', 'r') as file1:
  iplist = file1.readlines()

  cleaned_iplist = []
  for line in iplist:
      rem_ip = line.replace('No new IP', '').replace('\n', '')
      if rem_ip != '':
          cleaned_iplist.append(rem_ip)

  
with open('file2.txt', 'w') as file2:
    dataline = file2.read()
    cleaned_iplist_2 = dataline.split(",")

    for line in cleaned_iplist_2:
      print(line)

file1.close()


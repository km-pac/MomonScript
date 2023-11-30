# CLEANING THE FIRST FILE FROM TWMON SHEET
with open('file1.txt', 'r') as file1:
  cleaned_iplist_twmon = []
  iplist = file1.readlines()
  for line in iplist:
      rem_ip = line.replace('No new IP', '').replace('\n', '')
      if rem_ip != '':
          cleaned_iplist_twmon.append(rem_ip)

  
with open('file2.txt', 'r') as file2:
    cleaned_iplist_momon = []
    dataline = file2.read()
    iplist = dataline.replace('[','').replace(']','').replace('"','').replace('\\','').split(",")
    cleaned_iplist_momon = [ip for ip in iplist if "\/" in ip]

    # for line in iplist:  
    #   if not line.isaplha():
    #     cleaned_iplist_momon.append(line)

  
    print(cleaned_iplist_momon)

    
        

file1.close()
file2.close()


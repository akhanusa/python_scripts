#!/usr/bin/python
import re

devlist = dict()

x = raw_input("Enter device name:")

y = x.strip()

devicesFile = open("/etc/device_profile", "r")

for line in devicesFile:
   if line.strip():
      if re.search(y,line.split("~")[1].strip(),re.IGNORECASE):
         devlist[line.split("~")[1]] = line.split("~")[0]
for dev in devlist:
   print dev + " : " + devlist[dev]

if len(devlist) > 1:
   flag = True
   while flag: 
      a = raw_input("Enter device name:")
      b = a.strip()
      counter = 0
      for i in devlist:
         c = re.search(b,str(i),re.IGNORECASE)
         if c:
            counter = counter + 1
            print i + ':' + ' ' + devlist[i]
      if counter < 2:
         flag = False
            
devicesFile.close()

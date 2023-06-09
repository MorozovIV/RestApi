import os
import current_time
hostname = "google.com" #example
response = os.system("ping -n 1 " + hostname) #windows
# response = os.system("ping -c 1 " + hostname) #linux
#and then check the response...
if response == 0:
  print(hostname, 'is up!')
  current_time.time()
else:
  print(hostname, 'is down!')
  print(None)


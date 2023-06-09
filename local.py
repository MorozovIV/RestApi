#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import os

hostname = "127.0.0.1" #example
response = os.system("ping -n 1 " + hostname)

#and then check the response...
if response == 0:
  print(hostname, 'is up!')
else:
  print(hostname, 'is down!')
res = requests.get("http://127.0.0.1:3000/api/main")
print(res.json())

# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:12:39 2023

@author: zhijiel
"""

import requests

URL = 'https://disc.gsfc.nasa.gov/api/jobs/results/64f534e8bd0b7cacadb48ddd'

FILENAME = 'root_zone_soil_wetness'

import requests
result = requests.get(URL)

try:
    result.raise_for_status()
    f = open(FILENAME,'wb')
    f.write(result.content)
    f.close()
    print('contents of URL written to '+FILENAME)
except:
    print('requests.get() returned an error code '+str(result.status_code))

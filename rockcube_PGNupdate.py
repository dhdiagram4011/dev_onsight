#!/usr/bin/python3

import requests
import json

def cubecall():
    rock_url='http://35.190.226.241:8080/resource/projects'
    response=requests.get(url=rock_url)
    print(response.status_code)
    print(response.text)
#    raw=response.raw
#    rockcube_name_result = raw.read()
#    return rockcube_name_result
   
cubecall()



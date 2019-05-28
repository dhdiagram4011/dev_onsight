#!/usr/bin/python3

import requests
import os
import json


def Project_Name_Get():
    get_url='http://35.194.207.38:8080/internal/projects'
    response=requests.get(get_url,params={'projectId':'string','projectName':'string'})
    print(response.status_code)
    print(response.text)



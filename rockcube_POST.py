#!/usr/bin/python3

import requests
import os
import json


##Almond Project Name List GET()

def Project_Name_Get():
    get_url='http://35.194.207.38:8080/internal/projects'
    response=requests.get(rock_url,params={'projectId':'string','projectName':'string'})
    print(response.status_code)
    print(response.text)
    post_name=map(lambda response:{'projectId':response['projectId'],'projectName':response['name']},response)
    headers={'Content-Type':'application/json'}
    data={'projects':[{'projectId':'string','projectName':'string'}]}
    print(data)
    response=requests.get(post_url,headers=headers, data=json.dumps(data))
    print(post_name)
    print(response.status_code)
    print(response.text)

Project_Name_Get()




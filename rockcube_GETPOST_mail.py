#!/usr/bin/python3

####
#Author:dohyoung.kim@rockplace.co.kr
#Modifier:dohyoung.kim@rockplace.co.kr

import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
import requests
import os

##Almond Project Name List GET()

def Project_Name_Get():
    rock_url='http://gcpapi:8080/resource/projects'
    post_url='http://auth:8080/internal/projects'
    response=requests.get(rock_url,params={'projectId':'string','projectName':'string','projectNumber':'string'})
    print(response.status_code)
    print(response.text)

Project_Name_Get()

      


##Almond Project Name POST()
## local is IP
## jenkins is service IP

response=requests.post('http://auth:8080/internal/projects',params={'projectId':'string','projectName':'string','projectNumber':'string'})
post_name=map(lambda response:{'projectId':response['projectId'],'projectName':response['name'],'projectNumber':response['projectNumber']},response)
print(post_name)
print(response.status_code)
print(response.text)


## API Post Step
response=requests.post('http://auth:8080/internal/projects',params=post_name)
print(response.status_code)
print(response.text)








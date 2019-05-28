#!/usr/bin/python3

import requests
import os
import json
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.header import Header
import codecs

get_url='http://auth:8080/internal/projects'
headers={'Content-type':'application/json'}
result_code=requests.get(get_url,headers=headers)
print(result_code.text)

if result_code.text in "200":
    result=os.system("curl -XGET -w %{http_code} http://auth:8080/internal/projects")
    r_code=print(result)
    noti_url="https://chat.googleapis.com/v1/spaces/AAAA5vM-DO8/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=XjZbQA-oKT8bgvnUyYs0V9k4VZI3LGojGbVPlEk2Yi4%3D"
    data={'text':'[rockcube]고객사 프로젝트 명 업데이트 완료'}
    mention_comment="Customer Project Name Update Complete!"
    headers={'Content-type':'application/json'}
    response=requests.post(noti_url,data=json.dumps(data), headers=headers)
    print(response)
    print(response.status_code)
    print(response.text)
    with open('name_result.txt','w') as f:
        f.write(mention_comment)
else:
    result=os.system("curl -XGET -w %{http_code} http://auth:8080/internal/projects")
    r_code=print(result)
    noti_url="https://chat.googleapis.com/v1/spaces/AAAA5vM-DO8/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=XjZbQA-oKT8bgvnUyYs0V9k4VZI3LGojGbVPlEk2Yi4%3D"
    data={'text':'[rockcube]고객사 프로젝트 업데이트 실패,확인필요'}
    mention_comment="Customer Project Name Upldate Failed"
    headers={'Content-type':'application/json'}
    response=requests.post(noti_url,data=json.dumps(data), headers=headers)
    print(response)
    print(response.status_code)
    print(response.text)
    with open('name_result.txt','w') as f:
        f.write(mention_comment)


rp_smtp = "smtp.gmail.com"
rp_port  = "587"
user_id = "rp_system@rockplace.co.kr"
user_passwd = "qobenukqcgnqtvff"

file = open("name_result.txt","r")
Document = MIMEText(file.read(),_charset='utf-8')
file.close()


def send_mail(from_user,to_user,cc_manager,subject,informtext,attach):
    COMMASPACE=","
    msg = MIMEMultipart("alternative")
    msg["from"] = from_user
    msg["to"] = to_user
    msg["cc"] = COMMASPACE.join(cc_manager)
    msg["subject"] = Header(s=subject, charset="utf-8")
    msg.attach(Document)
    

    smtp = smtplib.SMTP(rp_smtp,rp_port)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user_id,user_passwd)
    smtp.sendmail(from_user,cc_manager,msg.as_string())
    smtp.quit()


send_mail('rp_system@rockplace.co.kr','sdev@rockplace.co.kr',['sdev@rockplace.co.kr','sdev@rockplace.co.kr'],"[CPPROD]Daily Customer Projectname Update" , "[CPPROD]Daily Customer Projectname Update","name_result.txt")


















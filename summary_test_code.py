#!/usr/local/bin/python3
<<<<<<< HEAD

print("summary test code")
=======
#initial author : dohyoung.kim@rockplace.co.kr(Cloud Technology Division - Sdev Team)

import json
import os
import sys
import requests


#summary_test1 : cpdev.rockcube.co.kr user login test

caller_url='https://cpdev.rockcube.co.kr/oauthlogin?id=rockcube&password=rockcube!'
api_url='https://cpdev.rockcube.co.kr/api/users

headers={'Content-Type':'application/json'}

def summary_test():
    caller_url='https://cpdev.rockcube.co.kr/oauthlogin?id=rockcube&password=rockcube!'
    slack_url='https://hooks.slack.com/services/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'
    headers={'Content-Type':'application/json'}
    session=requests.Session()
    response=requests.get(caller_url,verify=False,headers=headers)
    print(caller_url)
    print(response)
    print(response.text)
    print(response.status_code)   

    if "200" in response:
        print('summary_test_step1.login test success!')
        data={'text':'통합테스트1단계 : 로그인 성공'}
        r=requests.post(slack_url,headers=headers,data=json.dumps(data))
    else:
        print('summary_test_step1.login test failed!')
        data={'text':'통합테스트1단계 : 로그인 실패'}
        r=requests.post(slack_url,headers=headers,data=json.dumps(data))
    

summary_test()


#summary_test2 : Customer user project list search

def customer_project_list_search():
    instance_search_url='https://cpdev.rockcube.co.kr/api/compute/projects/elegant-weaver-209800/instances'
    slack_url='https://hooks.slack.com/services/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'
    headers={'Content-Type':'application/json'}
    response=requests.get(instance_search_url,verify=False,headers=headers)
    print(response)
    print(response.text)
    print(response.status_code)

    if "200" in response.text:
        data={'text':'통합테스트2단계 : 프로젝트 리스트 조회 성공'}
        r=requests.post(slack_url,headers=headers,data=json.dumps(data))
    else:
        data={'text':'통합테스트2단계 : 프로젝트 리스트 조회 실패'}
        r=requests.post(slack_url,headers=headers,data=json.dumps(data))


customer_project_list_search()


#summary_test3 : summary test result send to slack
















>>>>>>> master



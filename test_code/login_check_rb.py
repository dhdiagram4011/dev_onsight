#!/usr/bin/python3

<<<<<<< HEAD:test_code/login_check_rb.py
#Before Deploy Login Check Code
#Author:dohyoung.kim@rockplace.co.kr
#Modifier:dohyoung.kim@rockplace.co.kr
#Last Modifier: 2018.12.13 <-> Slack Connect dohyoung.kim@rockplace.co.kr , RP Cloud Technical Division / Solution Deveolpment Team


import requests
import json
import os
import sys
=======
import json
import os
import sys
import requests

HOST = 'https://cpdev.rockcube.co.kr'
# HOST = 'http://localhost:8081'
>>>>>>> master:login_check.py

ID = 'rockcube'
PW = 'rockcube!'

LOGIN_API = HOST + '/oauthlogin?id={}&password={}'.format(ID,PW)
USER_API = HOST + '/api/user'

HEADERS={'Content-Type':'applicationi/json'}

<<<<<<< HEAD:test_code/login_check_rb.py
### GET (Step2. User Information GET)
def ldap_info_get():
    session = ''
    get_url='http://35.229.251.198/oauthlogin'
    post_url='http://35.229.251.198/api/user'
    headers={'Content-Type':'application/json'}
    cookie={'SESSION':'cubecookie'}
    getter=requests.get(get_url,headers=headers,cookies=cookie,params={'email':'rockcube','password':'rplinux88605'})
    for c in getter.cookies:
      if c.name == 'SESSION':
        session = c.value
    print(getter.status_code)
    print(getter.text)
    ### After Action
    if print(getter.text) == print("200"):
        print("checkok")
        ldap_user_info_text_gathering(session)
    else:
        print("rollback start!")


### GET (Step3. User Login Information Text Gathering & Slack Notification)
def ldap_user_info_text_gathering(session):

    get_url='http://35.229.251.198/api/user'
    post_url='https://hooks.slack.com/services/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'
    headers={'Content-Type':'application/json'}
    cookie={'SESSION':session}
    print(cookie)
    info_getter=requests.get(get_url,headers=headers,cookies=cookie)
    print(info_getter.status_code)
    print(info_getter.text)
    if "rockcube" in info_getter.text:
        print('login success!!!')
        bot_url="https://hooks.slack.com/services/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"
        data={'text':'login success!!!'}
        headers={'Content-Type':'application/json'}
        response=requests.post(bot_url,headers=headers,data=json.dumps(data))
    else:
        print('login failed!!! - RollBack START!!!')
        bot_url="https://hooks.slack.com/services/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"
        data={'text':'login failed!!!'}
        ##files={'file':('auth_history.txt').open('auth_history.txt','rb').'txt'}
        headers={'Content-Type':'application/json'}
        response=requests.post(bot_url,headers=headers,data=json.dumps(data))
        ##rollback start
        ##step1) rollback version 조회
        os.system("touch auth_history.txt")
        os.system("kubectl rollout history deployment auth")
        os.system("kubectl rollout history deployment auth > auth_history.txt")
        os.system("kubectl rollout history deployment auth | sed -n '13p' | awk '{print $1}') >> auth_history.txt")
        os.system("sleep 30;")
        ##step2) 해당 버전으로 롤백 시작
        os.system("echo rollback check logic success!!!")
        os.system("echo $(kubectl rollout history deployment auth | sed -n '13p' | awk '{print $1}' 버전으로 롤백합니다.) > rollback_number.txt")
        ###os.system("kubectl rollout undo deployment/auth --to-revision=$(kubectl rollout history deployment auth | sed -n '13p' | awk '{print $1}'")
=======
SLACK_URL = "https://hooks.slack.com/services/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"
>>>>>>> master:login_check.py

##def set_host():
##  env = sys.argv[1]

##  if( env == "local"):
##    HOST = "http://localhost:8081"
##  if( env == "dev"):
##    HOST = "https://cpdev.rockcube.co.kr/"

def login():
    print(LOGIN_API)
    response = requests.get(LOGIN_API,verify=False, headers=HEADERS)
    status_code = response.status_code
    print(status_code)
    if( status_code != 200 ):
      rollback()
      return

    session_value = get_session_value(response)
    print(response.text)
    call_user_api(session_value)

def call_user_api(session):
    response=requests.get(USER_API,verify=False,headers=HEADERS,cookies={'SESSION':session})
    rb_container_image=os.system("kubectl describe pods view | grep gcr.io | sed -n '1p' | awk '{print $2}'")
    print(rb_container_image)

    if "200" in response.text:
        send_message_to_slack('로그인 테스트 성공! 배포가 완료되었습니다.')
    else:
        rollback()


def rollback():
  send_message_to_slack('로그인 테스트 실패, 롤백 준비')
  #os.system("kubectl rollout undo deployment/view --to-revision=$(kubectl rollout history deployment view | sed -n '13p' | awk '{print $1}'")
  send_message_to_slack('로그인 테스트 실패, 롤백 완료. container name : ....')

  # rollback 내용을 보여주기 위한 기능
  # os.system("kubectl rollout history deployment view >> auth_history.txt")
  # os.system("echo kubernetes pod $(kubectl rollout history deployment view | sed -n '13p' | awk {'print $1'}) 버전으로 롤백합니다 >> auth_history.txt")
  # os.system("echo kubernetes pod rollback start >> auth_history.txt")

def send_message_to_image_name():
  data={'text':rb_container_image.data.decode('utf-8')}
  requests.post(SLACK_URL,verify=False,headers=HEADERS,data=data)

def send_message_to_slack(message):
  data={'text':message}
  requests.post(SLACK_URL,verify=False,headers=HEADERS,data=json.dumps(data))

def get_session_value(r):
  for c in r.cookies:
      if c.name == 'SESSION':
        return c.value

##set_host()
login()

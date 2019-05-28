#!/usr/bin/python3

import json
import os
import sys
import requests

HOST = 'https://cpdev.rockcube.co.kr'
# HOST = 'http://localhost:8081'

ID = 'rockcube'
PW = 'rockcube!'

LOGIN_API = HOST + '/oauthlogin?id={}&password={}'.format(ID,PW)
USER_API = HOST + '/api/user'

HEADERS={'Content-Type':'application/json'}

SLACK_URL = "https://hooks.slack.com/services/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"

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
    if status_code != 200:
      rollback()
      return

    session_value = get_session_value(response)
    call_user_api(session_value)

def call_user_api(session):
    response=requests.get(USER_API,verify=False,headers=HEADERS,cookies={'SESSION':session})
    rb_container_image=os.system("kubectl describe pods view | grep gcr.io | sed -n '1p' | awk '{print $2}'")
    print(rb_container_image)
    print(response.text)
    if "rockcube" in response.text:
        send_message_to_slack('로그인 테스트 성공! 배포가 완료되었습니다.')
    else:
        rollback()


def rollback():
  send_message_to_slack('로그인 테스트 실패, 롤백이 필요 합니다.')
  #os.system("kubectl rollout undo deployment/view --to-revision=$(kubectl rollout history deployment view | sed -n '13p' | awk '{print $1}'")
  send_message_to_slack('로그인 테스트 실패, 롤백 완료')

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

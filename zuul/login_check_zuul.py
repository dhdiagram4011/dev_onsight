# curl -u almondview:1fCt7BdlTV http://localhost:8080/api/auth/oauth/token?grant_type=password&username=rockcube&password=rockcube\!

#!/usr/local/bin/python3

import os
import sys
import requests
import json


ZUUL_TOKEN_API = '/api/auth/oauth/token'
ZUUL_USER_API = '/api/auth/me'

SLACK_URL = "https://hooks.slack.com/services/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"
HEADERS={'Content-Type':'applicationi/json'}

def zuul_login_test():

  host = get_host()

  token = get_auth_token(host)

  resUser = requests.get(host + ZUUL_USER_API, headers={'Authorization': 'Bearer {}'.format(token)})

  if "\"id\":100" in resUser.text:
    send_message_to_slack('로그인 테스트 성공! zuul 배포가 완료되었습니다.')

def get_host():
  if len(sys.argv) <= 1:
    return 'http://localhost:9999'

  if len(sys.argv) == 2:
    profile = sys.argv[1]
    return 'http://zuul:8080'

def get_auth_token(host):
  res = requests.post(host + ZUUL_TOKEN_API, auth=('almondview', '1fCt7BdlTV'), params = {'grant_type': 'password', 'username': 'rockcube', 'password': 'rockcube!'})
  data = json.loads(res.text)
  accessToken = data["access_token"]
  return accessToken

def send_message_to_slack(message):
  data={'text':message}
  requests.post(SLACK_URL,verify=False,headers=HEADERS,data=json.dumps(data))

zuul_login_test()
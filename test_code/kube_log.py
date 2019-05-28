#!/usr/local/bin/python3

import os
import sys
import json
import requests

#rockcube-mon-dev
#archdev_token='xoxp-467735474241-467620701664-502939042640-84f167bdb9d5364c1afcfde3cf6d78ab'

def kubectl_pod_logs():
    os.system('kubectl logs view-7c68df5477-b7trn | grep ERROR >> pod_log.txt')
    p_result=open("pod_log.txt",'r')
    pr=print(p_result.read())
    ###post_url='https://hooks.slack.com/services/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'
    ###token="xoxp-146049578305-241154099606-503017380229-5fa989ae3cb293fca28b5a1944ea2104" ###sdevtalk_token
    token='xoxp-467735474241-467620701664-502939042640-84f167bdb9d5364c1afcfde3cf6d78ab' ###archdev_token
    post_url='https://slack.com/api/files.upload?token=xoxp-467735474241-467620701664-502939042640-84f167bdb9d5364c1afcfde3cf6d78ab'
    #post_url='https://hooks.slack.com/services/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'
    headers={'Content-Type':'application/x-www-form-urlencoded'}
    files={'file':('pod_log.txt',open('pod_log.txt','rb'),'txt')}
    payload={"fname":"pod_status.txt","channels":["#rockcube-mon-dev"],"tokens":token,"media":files}
    response=requests.post(post_url,params=payload,files=files)
    print(response)
    print(response.status_code)
    print(response.text)


kubectl_pod_logs()





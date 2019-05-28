#!/usr/local/bin/python3

import os
import sys
import json
import requests

##Channel Name
#rockcube-chatops
#rockcube-cicd-dev
#rockcbue-cicd-prod
#rockcube-deploy-dev
#rockcube-deploy-prod
#rockcube-mon-dev
#rockcube-mon-prod
#archdev_token='xoxp-467735474241-467620701664-502939042640-84f167bdb9d5364c1afcfde3cf6d78ab'

def kubectl_status():
    os.system('kubectl get pods > pod_status.txt')
    p_result=open("pod_status.txt",'r')
    pr=print(p_result.read())
    ###post_url='https://hooks.slack.com/services/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'
    ###token="xoxp-146049578305-241154099606-503017380229-5fa989ae3cb293fca28b5a1944ea2104" ###sdevtalk_token
    token='xoxp-467735474241-467620701664-502939042640-84f167bdb9d5364c1afcfde3cf6d78ab' ###archdev_token
    post_url='https://slack.com/api/files.upload?token=xoxp-467735474241-467620701664-502939042640-84f167bdb9d5364c1afcfde3cf6d78ab'
    #post_url='https://hooks.slack.com/services/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'
    headers={'Content-Type':'application/x-www-form-urlencoded'}
    files={'file':('pod_status.txt',open('pod_status.txt','rb'),'txt')}
    payload={"fname":"pod_status.txt","channels":["#rockcube-mon-prod"],"tokens":token,"media":files}
    response=requests.post(post_url,params=payload,files=files)
    print(response)
    print(response.status_code)
    print(response.text)


kubectl_status()





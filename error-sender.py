#!/usr/local/bin/python3

###Author: dohyoung.kim@rockplace.co.kr 
###Initial Dev : 2019.01.07


import os
import sys
import requests

###rockcube-app-error-logger.py

def error_logger():
    os.system('python3 rockcube-app-error-logger.py > app-error-logger.txt')
    log_result=open("app-error-logger.txt",'rb')
    logger=print(log_result.read())
    ###post_url='https://hooks.slack.com/services/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'
    token='xoxp-467735474241-467620701664-502939042640-84f167bdb9d5364c1afcfde3cf6d78ab' ###archdev_token
    post_url='https://slack.com/api/files.upload?token=xoxp-467735474241-467620701664-502939042640-84f167bdb9d5364c1afcfde3cf6d78ab'
    headers={'Content-Type':'application/x-www-form-urlencoded'}
    files={'file':('app-error-logger.txt',open('app-error-logger.txt','rb'),'txt')}
    payload={"fname":"app-error-logger.txt","channels":["#rockcube-error-dev"],"tokens":token,"media":files}
    response=requests.post(post_url,params=payload,files=files)
    print(response)
    print(response.status_code)
    print(response.text)

error_logger()

#!/usr/local/bin/python3

import os
import sys
##import json
##import requests
import time
import google.cloud 
from google.cloud import pubsub_v1

##Define Channel Name
#rockcube-chatops
#rockcube-cicd-dev
#rockcbue-cicd-prod
#rockcube-deploy-dev
#rockcube-deploy-prod
#rockcube-mon-dev
#rockcube-mon-prod
#archdev_all_token='xoxp-467735474241-467620701664-502939042640-84f167bdb9d5364c1afcfde3cf6d78ab'
#topics=app-error

#Variation Define

project_id='elegant-weaver-209800'
subscription_name='rocube-error-sub'

subscriber=pubsub_v1.SubscriberClient()
subscription_path=subscriber.subscription_path(project_id,subscription_name)

def callback(message):
    print('Received message: {}' .format(message))
    message.ack()

subscriber.subscribe(subscription_path, callback=callback)

print('Listening for message on {}' .format(subscription_path))



##def error_logger():
#    os.system('kubectl get pods > pod_status.txt')
#    p_result=open("pod_status.txt",'r')
#    pr=print(p_result.read())
#    ###post_url='https://hooks.slack.com/services/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'
#    ###token="xoxp-146049578305-241154099606-503017380229-5fa989ae3cb293fca28b5a1944ea2104" ###sdevtalk_token
#    token='xoxp-467735474241-467620701664-502939042640-84f167bdb9d5364c1afcfde3cf6d78ab' ###archdev_token
#    post_url='https://slack.com/api/files.upload?token=xoxp-467735474241-467620701664-502939042640-84f167bdb9d5364c1afcfde3cf6d78ab'
    #post_url='https://hooks.slack.com/services/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'
#    headers={'Content-Type':'application/x-www-form-urlencoded'}
#    files={'file':('pod_status.txt',open('pod_status.txt','rb'),'txt')}
#    payload={"fname":"pod_status.txt","channels":["#rockcube-mon-prod"],"tokens":token,"media":files}
#    response=requests.post(post_url,params=payload,files=files)
#    print(response)
#    print(response.status_code)
#    print(response.text)


#error_logger()





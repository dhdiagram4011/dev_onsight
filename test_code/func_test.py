#!/usr/local/bin/python3

import requests
import os
import sys
import json

def slack_noti():
    bot_url="https://hooks.slack.com/services/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"
    data={'text':'success'}
    headers={'Content-Type':'application/json'}
    ###post_name=map(lambda response:{'text':response['text']},response)
    response=requests.post(bot_url,headers=headers,data=json.dumps(data))
    print(response)
    print(response.status_code)
    print(response.text)


slack_noti()









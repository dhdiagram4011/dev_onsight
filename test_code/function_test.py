#!/usr/local/bin/python3


import requests
import google.cloud 
import json
from google.cloud import pubsub_v1


SLACK_URL = "https://hooks.slack.com/services/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"

def send_message_to_slack(message):
    try:
        print("start")
        print(message.data)
        url = "https://hooks.slack.com/services/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"
        data = {'text':message.data.decode('utf-8')}
        headers = {'Content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        print(r)
    except Exception as e:
        print(e)

def callback(message):
    print('Received message: {}' .format(message.data))
    send_message_to_slack(message)
    message.ack()





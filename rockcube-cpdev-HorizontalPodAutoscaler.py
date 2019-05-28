#!/usr/local/bin/python3


import requests
import google.cloud 
import json
from google.cloud import pubsub_v1


project_id="elegant-weaver-209800"
subscription_name="HorizontalPodAutoscaler"



subscriber=pubsub_v1.SubscriberClient()
subscription_path=subscriber.subscription_path(project_id,subscription_name)

while True:
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

    future=subscriber.subscribe(subscription_path, callback=callback)


    try:
        future.result(timeout=60)
    except Exception as e:
        print('Listening for messages on {} threw an Exception: {}.'.format(subscription_name,e))

    
    subscriber.subscribe(subscription_path, callback=callback)
    print('Listening for messages on {}' .format(subscription_path))


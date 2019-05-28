#author:dohyoung.kim@rockplace.co.kr - Cloud Technical Division in RPITS Team

import requests
import os 
import sys
import subprocess
import json

os.system("gcloud container clusters get-credentials cpdev --zone asia-east1-b --project elegant-weaver-209800")

rockcube_pod_status_check="kubectl get pods"
Notification_URL='https://hooks.slack.com/services/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'


rockcube_pod_status_check=subprocess.check_output('kubectl get pods',universal_newlines=True, shell=True)

print(rockcube_pod_status_check)


def pod_check():
    pod_check_result={"text":rockcube_pod_status_check}
    headers={'Content-Type':'application/json'}
    response=requests.post(Notification_URL,data=json.dumps(pod_check_result))
    print(response.text)
    print(response.status_code)
    if "Evicted" in response.text:
        evicted_check={"text":"Evicted Pod 발생"}
        headers={'Content-Type':'application/json'}
        response=requests.post(Notification_URL,data=json.dumps(evicted_check))
    else:
        evicted_check={"text":"Evicted Pod 없음"}
        headers={'Content-Type':'application/json'}
        response=requests.post(Notification_URL,data=json.dumps(evicted_check))


pod_check()













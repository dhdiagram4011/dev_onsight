#!/usr/local/bin/python3

###gcloud container images list-tags gcr.io/elegant-weaver-209800/rockcube/dev/billing --limit=999999 --sort-by=TIMESTAMP
###gcloud container images list-tags gcr.io/elegant-weaver-209800/rockcube/dev/python --limit=999999 --sort-by=TIMESTAMP --filter="timestamp.datetime < '${DATE}'"

import os
import json
import requests
import subprocess
import sys
import datetime


alert_url='https://hooks.slack.com/services/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'
headers={'Content-Type':'application/json'}
gcr_list_title={"text":"gcr.io 리스트"}
gcr_delete_list_title={"text":"gcr.io 삭제대상리스트"}

now=datetime.datetime.now()

nowDate=now.strftime('%Y-%m-%d')
print(nowDate)


gcr_list=subprocess.check_output('gcloud container images list-tags gcr.io/elegant-weaver-209800/rockcube/dev/billing --limit=999999 --sort-by=TIMESTAMP', universal_newlines=True, shell=True)
gcr_datetime_list=subprocess.check_output('gcloud container images list-tags gcr.io/elegant-weaver-209800/rockcube/dev/billing --limit=999999 --sort-by=TIMESTAMP --filter=timestamp.datetime', universal_newlines=True,shell=True)

print(gcr_list)
print(gcr_datetime_list)

todays=print(nowDate)


gcr_delete_list=subprocess.check_output('gcloud container images list-tags gcr.io/elegant-weaver-209800/rockcube/dev/billing --limit=999999 --sort-by=TIMESTAMP --filter="timestamp.datetime > `date +%Y-%m-%d`"' ,universal_newlines=True,shell=True)

#sample_date
##gcloud container images list-tags gcr.io/elegant-weaver-209800/rockcube/dev/billing --limit=999999 --sort-by=TIMESTAMP --filter="timestamp.datetime > '${DATE}'"

print(gcr_datetime_list)

gcr_lst={"text":gcr_list}
gcr_del_list={"text":gcr_delete_list}


response=requests.post(alert_url,data=json.dumps(gcr_list_title))
response=requests.post(alert_url,data=json.dumps(gcr_lst))

response=requests.post(alert_url,data=json.dumps(gcr_delete_list_title))
response=requests.post(alert_url,data=json.dumps(gcr_del_list))













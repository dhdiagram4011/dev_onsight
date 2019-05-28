import requests
import threading
import json


HEADERS={'Content-Type':'applicationi/json'}

def gcp_call():
  print("call gcp")
  res = requests.get('http://35.229.251.198:8080/monitoring/projects/projects/timeSeries?projectIds=synthetic-time-171501,zinc-fold-201301,elegant-weaver-209800,stellar-envoy-211306,static-grid-211306,soy-analog-207301,storied-precept-206504,robust-limiter-195815,cobalt-particle-224006&filters=metric.type+%3D+%22compute.googleapis.com%2Finstance%2Fcpu%2Futilization%22%3BALIGN_MEAN%3BREDUCE_MEAN,metric.type+%3D+%22cloudsql.googleapis.com%2Fdatabase%2Fcpu%2Futilization%22%3BALIGN_MEAN%3BREDUCE_MEAN,metric.type+%3D+%22appengine.googleapis.com%2Fsystem%2Fmemory%2Fusage%22%3BALIGN_MEAN%3BREDUCE_MEAN&startTimestamp=1547614689&endTimestamp=1548219489&duration=3600&groupBy=project',verify=False, headers=HEADERS)
  print(res.text)

def auth_call():
  print("call auth")
  res = requests.get('http://35.229.133.212:8080/admin/exchanges',verify=False, headers=HEADERS)
  print(res.text)

for x in range(300):
  print("start auth:", x)
  t1 = threading.Thread(target=auth_call)
  t1.start()
  print("start gcp:", x)
  t2 = threading.Thread(target=gcp_call)
  t2.start()


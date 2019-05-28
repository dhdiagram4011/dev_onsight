#!/usr/local/bin/python3


from google.cloud import monitoring_v3
import numpy as np

def cpdev_uptime_check_ip_list():
    region_list= ["region","location","ip_address"]
    uptime_date=np.array([[ip.region,ip.location,ip.ip_address]])


cpdev_uptime_check_ip_list()


   

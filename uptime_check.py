#!/usr/local/bin/python3

from __future__ import print_function
import argparse
import os
import pprint

from google.cloud import monitoring_v3
import tabulate

def cpdev_uptime_check_ip_list():
    client=monitoring_v3.UptimeCheckServiceClient()
    iplist=client.list_uptime_check_ips()
    print(tabulate.tabulate(
        [(ip.region, ip.location, ip.ip_address) for ip in iplist],
        ('region','location','ip_address')
    ))


cpdev_uptime_check_ip_list()


   

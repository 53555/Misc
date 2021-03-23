#!/usr/bin/python

# The script prints information about all Artemis queues
# Artemis server / jolokia is localhost
# Script is designed to be run on Artemis Server / ECS node 1
#
# Script is compatible to python 2 and 3

import sys

if sys.version_info[0] == 2:
    from urllib2 import urlopen
else:
    from urllib.request import urlopen
import json
import re

HOSTNAME = 'localhost'
PORT = 8161
BASEURL = 'http://' + HOSTNAME + ':' + str(PORT) + '/jolokia/'
ARTEMIS = 'org.apache.activemq.artemis'


def getBeans():
    response = urlopen(BASEURL + 'list/' + ARTEMIS)
    beans = json.load(response)['value'].keys()
    return beans


def getAttributes(queue_path):
    response = urlopen(BASEURL + 'read/' + ARTEMIS + ':' + queue_path)
    attribs = json.load(response)['value']
    return attribs


queue_re = re.compile('address="jms\.queue')

for bean in getBeans():
    if queue_re.search(bean):
        attribs = getAttributes(bean)
        print("Queue: " + attribs["Name"])
        for (name, value) in attribs.items():
            if name != 'Name':
                print("    " + name + ': ' + str(value))

#!/usr/bin/env python2.7

import globals
import os, glob, operator
import time
import sys
import thread
import urllib2
from alarmfunctionsr import GetDataFromHost
from time import sleep

# Globals

thermostatTemp = 80

# This is for your PrivateEyePi username, password. Change accordingly
globals.user='johnsmith@foobar.com'
globals.password='allthecoolkidspeetheirpants'
globals.PrintToScreen = True

# Switches
# These RF Codes are for my outlets - you will have to sniff for yours
# See https://github.com/timleland/rfoutlet
#
sw1on = os.system('sudo ./rfoutlet/codesend 87347')
sw1off = os.system('sudo ./rfoutlet/codesend 87356')

sw2on = os.system('sudo ./rfoutlet/codesend 87491')
sw2off = os.system('sudo ./rfoutlet/codesend 87500')

sw3on = os.system('sudo ./rfoutlet/codesend 87811')
sw3off = os.system('sudo ./rfoutlet/codesend 87820')

sw4on =  os.system('sudo ./rfoutlet/codesend 89347')
sw4off = os.system('sudo ./rfoutlet/codesend 89356')

sw5on = os.system('sudo ./rfoutlet/codesend 95491')
sw5off = os.system('sudo ./rfoutlet/codesend 95500')

def compareTemp():
record = GetDataFromHost(21,[0])
    record = record[0]
    rec = record[2]
    temp = int(float(rec))
    if temp > thermostatTemp:
        os.system('sudo ./codesend 87491')
    if temp <= thermostatTemp:
        os.system('sudo ./codesend 87500')
    else:
        print "could not find temperature"

if __name__ == '__main__':
    compareTemp()
else:
    print "I am being imported for the first time"

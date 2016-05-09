#!
import os, glob, operator
import globals
import time
import sys
import thread
import urllib2
from alarmfunctionsr import GetDataFromHost
from time import sleep

#global

thermostatTemp = 80


# Switches
1on = 87347
1off = 87356

2on = 87491
2off = 87500

3on = 87811
3off = 87820

4on =  89347
4off = 89356

5on = 95491
5off = 95500


def getTemp():
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

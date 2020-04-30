import json
import os
import datetime


def parseAmount(amount):
	v = str(round(float(amount), 2))
	if len(v.split(".")) == 1:
		v += '.'
	while len(v.split('.')[1]) < 2:
		v += '0'
	return v + 'EUR'

def readConfig(key):
	config = json.loads(open(os.path.join(os.path.dirname(__file__), "config.json"),'r').read())
	return config[key]

def readBackup():
	return parseAmount(open(readConfig('rootFolder') + "lastvalue.txt", 'r').read())

def printDate():
	return datetime.datetime.now().strftime("%A, %d %B %Y om %H:%M")

def writeLog(txt):
	logfile = open(readConfig('rootFolder') + "log.txt", 'a')
	logfile.write(printDate() + ": " + txt + "\n")
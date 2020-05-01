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

def shortDate():
	return datetime.datetime.now().strftime("%d-%m-%Y")

def createFolder(dir):
	if not os.path.exists(dir):
		os.mkdir(dir)

def writeLog(txt):
	createFolder(readConfig('rootFolder') + "logs")
	fn = readConfig('rootFolder') + "/logs/" + shortDate() + ".txt"
	if os.path.exists(fn):
		logfile = open(fn, 'a')
	else:
		logfile = open(fn, 'w')
	logfile.write(printDate() + ": " + txt + "\n")
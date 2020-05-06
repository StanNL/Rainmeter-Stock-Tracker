import json
import datetime
import urllib.request
from fileManager import readConfig, writeLog, readBackup, parseAmount

def loadURL(url):
	return urllib.request.urlopen(url).read().decode("utf-8")


# Feel free to change this to other APIs than alphavantage
# The function should, however, return the following:
# 		(price, success, datetime)
# where:
#   price indicates the price that was retrieved
#   success indicates whether the price was read from backup, or live from the remote API
#   datetime (only when price was read from remote) indicates the date at which the stock price was live. As of right now, the time in this datetime object must be zero.
def loadPrice(): 
	response = loadURL('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&apikey=' + readConfig('api_key') + '&symbol=INGA.AMS&outputsize=compact&datatype=json')
	d = json.loads(response)

	if 'Global Quote' not in d:
		writeLog("ERROR! API limit reached. Reading from backup...")
		return (readBackup(), False, None)
	else:
		contents = d['Global Quote']
		for k in contents.keys():
			if len(k.split("price")) > 1:
				price = contents[k]
			if len(k.split("latest")) > 1:
				date = contents[k]

		if k is not None:
			writeLog("Successfully retrieved value " + price + 'EUR from remote.')
			return (price, True, datetime.datetime.strptime(date, "%Y-%m-%d"))
		else:
			writeLog("FOUT! Hier gebeurde iets heel geks...")
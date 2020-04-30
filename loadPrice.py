import json
import urllib.request
from files import readConfig, writeLog, readBackup, parseAmount

def loadURL(url):
	return urllib.request.urlopen(url).read().decode("utf-8")


# Feel free to change this to other APIs than alphavantage
# The function should, however, return the following:
# 		(price, success)
# where success indicates whether the price was read from backup, or live from the remote API
def loadPrice(): 
	response = loadURL('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&apikey=' + readConfig('api_key') + '&symbol=INGA.AMS&outputsize=compact&datatype=json')

	contents = json.loads(response)['Global Quote']

	if contents is None:
		writeLog("ERROR! API limit reached.")
		return (readBackup(), False)
	else:
		for k in contents.keys():
			if len(k.split("price")) > 1:
				price = contents[k]

		if k is not None:
			writeLog("Successfully retrieved value " + price + ' from origin.')
			return (price, True)
		else:
			writeLog("FOUT! Hier gebeurde iets heel geks...")
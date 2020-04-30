import datetime
from files import readConfig, readBackup, printDate, writeLog, parseAmount
from loadPrice import loadPrice

rootFolder = readConfig('rootFolder')

try:
	t = datetime.datetime.now()
	if (t.hour > readConfig("closingHour") or (t.hour is readConfig('closingHour') and t.min > readConfig("closingMinutes"))) or (t.hour < readConfig("openingHour") or (t.hour is readConfig("openingHour") and t.min < readConfig('openingMinutes'))) :
		print(readBackup())
		writeLog(printDate() + ": Exchange closed! Read from backup.")
	else:
		apicall = loadPrice()
		price = apicall[0]
		success = apicall[1]
		print(parseAmount(price))
		if success:
			backup = open(rootFolder + "lastValue.txt", 'w')
			backup.write(price)
except Exception as err:
	writeLog("ERROR! Unknown error: " + str(err))

import datetime
import re
from fileManager import readConfig, readBackup, printDate, writeLog, parseAmount, setColour
from loadPrice import loadPrice

rootFolder = readConfig('rootFolder')

try:
	t = datetime.datetime.now()
	oh = readConfig('openingHour') if readConfig('openingHour') is not None else 00
	ch = readConfig('closingHour') if readConfig('closingHour') is not None else 23
	om = readConfig('openingMinutes') if readConfig('openingMinutes') is not None else 00
	cm = readConfig('closingMinutes') if readConfig('closingMinutes') is not None else 59

	beforeHours = (t.hour < oh or (t.hour is oh and t.minute < om))
	afterHours = (t.hour > ch or (t.hour is ch and t.minute > cm))
	weekend = (datetime.datetime.now().weekday() + 1) in (readConfig("closedDays") or [])

	if beforeHours or afterHours or weekend:
		print(readBackup())
		writeLog(printDate() + ": Exchange closed! Read from backup.")
	else:
		apicall = loadPrice()
		price = apicall[0]
		success = apicall[1]
		stocktime = apicall[2]
		print(parseAmount(price))
		if success:
			red = "255, 0, 0"
			green = "0, 255, 0"
			white = "255, 255, 255"
			backupfile = open(rootFolder + "lastValue.txt", 'r')
			oldBackup = backupfile.read()
			backupfile.close()
			if oldBackup.split('\n')[1] == str(datetime.datetime.combine(datetime.datetime.now().date(), datetime.datetime.min.time())):
				#stock was last updated today
				oldV = float(re.sub('[a-zA-Z]', '', oldBackup.split('\n')[0]))
				newV = float(re.sub('[a-zA-Z]', '', price))
				if oldV > newV:
					setColour(red)
					open(rootFolder + 'color.txt', 'w').write(red)
				else:
					if oldV < newV:
						setColour(red)
					else:
						setColour(white)
						open(rootFolder + 'color.txt', 'w').write(white)
			else:
				setColour(white)

			backup = open(rootFolder + "lastValue.txt", 'w')
			backup.write(price + '\n' + str(stocktime))

except Exception as err:
	writeLog("ERROR! Unknown error: " + str(err))

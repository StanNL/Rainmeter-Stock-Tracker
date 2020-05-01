import datetime
import re
from fileManager import readConfig, readBackup, printDate, writeLog, parseAmount, setColour
from loadPrice import loadPrice

rootFolder = readConfig('rootFolder')

try:
	t = datetime.datetime.now()
	oh = readConfig('openingHour')
	ch = readConfig('closingHour')
	om = readConfig('openingMinutes')
	cm = readConfig("closingMinutes")

	beforeHours = (t.hour < oh or (t.hour is oh and t.minute < om))
	afterHours = (t.hour > ch or (t.hour is ch and t.minute > cm))

	if beforeHours or afterHours:
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

import datetime
import re
import sys
from sys import argv
import os
from fileManager import readConfig, readBackup, printDate, writeLog, parseAmount, setColour
from loadPrice import loadPrice

rootFolder = readConfig('rootFolder')
red = "255, 0, 0"
green = "0, 255, 0"
white = "255, 255, 255"


def retrieveRemote():
    apicall = loadPrice()
    price = apicall[0]
    success = apicall[1]
    stocktime = apicall[2]
    openV = apicall[3]
    prevC = apicall[4]
    print(parseAmount(price))
    if success:
        if(len(apicall) < 4):
            setColour(white)
        else:
            if(float(prevC) > float(price) + 0.01):
                setColour(red)
            else:
                if(float(prevC) < float(price) - 0.01):
                    setColour(green)
                else:
                    setColour(white)
        backup = open(rootFolder + "lastValue.txt", 'w')
        backup.write(parseAmount(price) + '\n' + str(stocktime))
    else:
        setColour(white)
        backupv = readBackup()
        writeLog("Retrieved value " + backupv + " from backup.")
        print(backupv)


try:
    if len(argv) > 1 and argv[1] == "middleClick":
        writeLog("Force-refreshing because of right click!")
        retrieveRemote()
    else:
        t = datetime.datetime.now()
        oh = readConfig('openingHour') if readConfig(
            'openingHour') is not None else 00
        ch = readConfig('closingHour') if readConfig(
            'closingHour') is not None else 23
        om = readConfig('openingMinutes') if readConfig(
            'openingMinutes') is not None else 00
        cm = readConfig('closingMinutes') if readConfig(
            'closingMinutes') is not None else 59

        beforeHours = (t.hour < oh or (t.hour is oh and t.minute < om))
        afterHours = (t.hour > ch or (t.hour is ch and t.minute > cm))
        weekend = (datetime.datetime.now().weekday() +
                   1) in (readConfig("closedDays") or [])

        if beforeHours or afterHours or weekend:
            print(readBackup())
            setColour(white)
            writeLog("Exchange closed! Read from backup.")
        else:
            retrieveRemote()

except Exception as err:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    writeLog("ERROR! Unknown error: " + str(err) +
             ". This error occured on line " + str(exc_tb.tb_lineno) + " in file " + fname)

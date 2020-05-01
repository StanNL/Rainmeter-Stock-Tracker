import webbrowser
from fileManager import readConfig
webbrowser.open("https://google.com/search?q=" + readConfig("stockName"))
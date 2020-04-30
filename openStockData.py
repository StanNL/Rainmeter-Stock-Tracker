import webbrowser
from files import readConfig
webbrowser.open("https://google.com/search?q=" + readConfig("stockName"))
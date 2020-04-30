# Rainmeter Stock Tracker
A small project for adding a stock-tracking Rainmeter skin. You can read more about Raimeter [here](https://www.rainmeter.net).

## Prerequisities
* A recent Rainmeter installation which you can download [here](https://www.rainmeter.net).
* A python3 installation, preferably running Windows (not tested on other operating systems).
## Installation instructions
- First, you install the skin to your system by unzipping a release (which you can find [here](https://github.com/StanNL/Rainmeter-Stock-Tracker/releases)), to your Rainmeter/Skins folder (which is likely in %userprofile%/Documents).
	- You can read more on installing new skins in the [official Rainmeter installation documentation](https://docs.rainmeter.net/manual/installing-skins/#InstallManually)
- Then, all that's left to do is open "config.json" and changing values as you wish.
	- You can change the root folder, which is where all logs and other information will be stored. I would recommend setting this to the same folder where you've installed the skin itself, so in all likelihood you'll want to chnage this to "%userprofile%\\\\Documents\\\\Rainmeter\\\\Skins\\\\Stocks\\\\".
	- In stockName, you can, as you may have expected, insert the name of the stock which you wish to track.
	- In openingHour, openingMinutes, closingHour and closingMinutes, you tell when your stock exchange opens and closes (in your system time). 
	- The actual retrieving is a little more complex however. You have two options
		* By default, the stock tracker uses Alpha Vantage's API for retrieving stock information. If you wish to continue using this API, all you then have to do is change "api_key" to your Alpha Vantage API key. If you do not have an API key, you can obtain one for free [here](https://www.alphavantage.co/support/#api-ke).
		* You are free to use whichever stock-tracking API you want. If you wish to abstain from using Alpha Vantage, you can change the file loadPrice.py accordingly. Instructions on what kind of information to return is available there.
# Rainmeter Stock Tracker
A small project for adding a stock-tracking Rainmeter skin. You can read more about Raimeter [here](https://www.rainmeter.net).

## Prerequisities
* A recent Rainmeter installation which you can download [here](https://www.rainmeter.net).
* A python3 installation, preferably running Windows (not tested on other operating systems).
## Installation instructions
- First, you install the skin to your system by unzipping a release (which you can find [here](https://github.com/StanNL/Rainmeter-Stock-Tracker/releases)), to your Rainmeter/Skins folder (which is likely in your user's ``Documents`` folder).
	- You can read more on installing new skins in the [official Rainmeter installation documentation](https://docs.rainmeter.net/manual/installing-skins/#InstallManually).
- Then, all that's left to do before placing the skin on your desktop, is opening "config.json" and changing values as you wish.
	- You can read more about the configuration of the program below, under ``Configuration Options``.
	- The actual retrieving of the data is a bit complex, sadly. You have two options:
		* By default, the stock tracker uses Alpha Vantage's API for retrieving stock information. If you wish to continue using this API, all you then have to do is change `api_key` in ``config.json`` to your Alpha Vantage API key. If you do not have an API key, you can obtain one for free [here](https://www.alphavantage.co/support/#api-ke).
		* You are free to use whichever stock-tracking API you want. If you wish to abstain from using Alpha Vantage, you can change the file ``loadPrice.py`` accordingly. Instructions on what kind of information to return is available there.
- Lastly, you'll want to add the skin to your Desktop. If you're not familiar with Rainmeter, you can read more on that [here](https://docs.rainmeter.net/manual/getting-started/using-rainmeter/#ContextMenu) (under ``Loading and Unloading``).

## Configuration Options
* Firstly, if you want you can customize the way the API loads data. In fact, you can use any API you want, though some might be a little more difficult to implement. As described above, you can change ``loadPrice.py`` as you wish, but be sure you know what you're doing!
* You can change ``config.json`` to suit your likings. You can change the following properties:
	* ``api_key`` (string): You can enter your stock-tracking API key here, as described above.
	* ``closedDays`` (array of Numbers): The weekdays at which your stock exchange is closed, i.e. ```[1, 4]``` would mean your stock exchange is closed every Monday and Thursday.
	* ``closingHour``, ``closingMinute``, ``openingHour`` and ``openingMinute`` all refer to the time at which your stock exchange opens and closes. **Beware**: The program uses your system's time! So if you want to track a stock outside of your timezone, be sure to change these values to your local time. For example, if your GMT+0 stock exchange opens at ``9:00`` and closes at ``17:30``, but you live in GMT+1, your config values would be: 
		* ``closingHour``: *18*,
		* ``closingMinute``: *30*,
		* ``openingHour``: *10*,
		* ``openingMinute``: *0*.
		* The reason why this matters (sometimes, that is) is because many (free) stock-tracking APIs have limits, and you dont want to send out too many requests to your server. If you for some reason want to send out API requests every minute of the day, you could remove these four lines altogether.
	* ``stockName`` is the name/symbol of the stock that is retrieved, like ```AAPL``` or ```INGA.AMS```.
	* ``rootFolder`` is the name of the folder where all the logs and information are stored. This folder should be the same as the location where you installedd the skin, so probably (on Windows):

			C:\\Users\\<your username>\\Documents\\Rainmeter\\Skins\\Stocks
		* Beware of two things however! Your slashes should in fact be double (so ``\\``) **and**, of course, you should replace ``<your username>`` by your Windows username. 
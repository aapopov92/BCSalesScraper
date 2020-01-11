<h2 align="center">Backcountry.com paddling gear scraper<h2>
![](https://i.imgur.com/xyEAmi6.png)
<h3 align="center">Requirements:</h3>
- Python 3.6+
- beautifulsoup4 4.8.2
- requests==2.22.0

------------
<h3 align="center">How to run it on Mac/Linux?</h3>
1. Install python 3.6+
2. [Install pip](https://pip.pypa.io/en/stable/installing/ "Install pip")
3. Checkout this repo
4. Go to folder with project
5. `chmod +x main.py`
6. `pip install -r requirements.txt`
7. `./main.py`

<h3 align="center">No, on Windows!</h3>
1. Get Linux, lol :)

TODO: Proper instruction

------------

<h3 align="center">What it does?</h3>
Parses backcountry.com paddling gear and places all products in local SQL DB each 30 minutes. And writes any new products to log. 


------------

<h3 align="center">Any next steps?</h3>
1. Do not hardcode parsing links. Move them to file.
2. Catch new sales!
3. Notifly about new sales via email
4. Notifly about new sales via Telegram bot
5. Add ability to choose categories in bot



## Backcountry.com paddling gear scraper 
![](https://i.imgur.com/xyEAmi6.png)

------------
### Requirements:
- Python 3.6+
- beautifulsoup4 4.8.2
- requests==2.22.0
------------
### How to run it on Mac/Linux?
1. Install python 3.6+
2. [Install pip](https://pip.pypa.io/en/stable/installing/ "Install pip")
3. Checkout this repo
4. Go to folder with project
5. `chmod +x main.py`
6. `./main.py`

### No, on Windows!
1. Get Linux, lol :)

TODO: Proper instruction

------------

### What it does?
Parses backcountry.com paddling gear and places all products in local SQL DB each 30 minutes. And writes any new products to log. 


------------

### Any next steps?
1. Do not hardcode parsing links. Move them to file.
2. Catch new sales!
3. Notifly about new sales via email
4. Notifly about new sales via Telegram bot
5. Add ability to choose categories in bot



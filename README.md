Telegram Message Cleaner
========================

**Telegram Message Cleaner** is a python script that can remove all your messages from specified chat.

Requirements
------------

-   Python 3.6 or higher
-   `telethon`

Installing
----------

Clone it or download manually.
```shell
    git clone https://github.com/S0Ulle33/telegram-message-cleaner.git
    cd telegram-message-cleaner
```

Install using system pip
```shell
    pip install -r requirements.txt
```
or using pipenv.
```shell
    pipenv install
```

Usage
-----

Before working with Telegram’s API, you need to get your own API ID and hash:

1. Follow this [link](https://my.telegram.org/) and login with your phone number.
2. Click under API Development tools.
3. A *Create new application* window will appear. Fill in your application details. There is no need to enter any URL, and only the first two fields (*App title* and *Short name*) can currently be changed later.
4. Click on *Create application* at the end. Remember that your **API hash is secret** and Telegram won’t let you revoke it. Don’t post it anywhere!
5. Launch `telegram_message_cleaner.py` and log in using your API ID and hash.
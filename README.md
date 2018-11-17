Telegram Message Cleaner
========================

**Telegram Message Cleaner** is a python script that can show your statistics (how many messages from you) on all your group chats, and also remove all your messages from specified chats.

Requirements
------------

-   Python 3.6 or higher
-   `telethon`
-   `prettytable`

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
5. Specify them in corresponding variables (`api_id` and `api_hash`) in `telegram_message_cleaner.py`

```
usage: telegram_message_cleaner_dev.py [-s [id id ...]] [-d [id id ...]]

Show stats for your messages in all/specified group chats
or delete all your messages in specified group chat(-s).

optional arguments:
  -h, --help            show this help message and exit
  -s [id [id ...]], --statistic [id [id ...]]
                        if you do not specify ID as an argument, it will show
                        stats of your messages for all group chats
  -d [id [id ...]], --delete [id [id ...]]
                        deletes all your messages from the specified group
                        chat ID(-s)

Examples:

1.Show stats for all your group chats:

    ./telegram_message_cleaner.py -s

    +------------+---------------+----------+
    |     ID     |     Group     | Messages |
    +------------+---------------+----------+
    | 1300197304 |   Work Group  | 234      |
    | 1210787553 | Bob and Alice | 75       |
    | 1274948231 |    Project    | 68       |
    +------------+---------------+----------+

2.Show stats only for 'Work Group' chat:

    ./telegram_message_cleaner.py -s 1300197304

    +------------+---------------+----------+
    |     ID     |     Group     | Messages |
    +------------+---------------+----------+
    | 1300197304 |   Work Group  | 234      |
    +------------+---------------+----------+

3.Show stats only for 'Bob and Alice' and 'Project' chats:

    ./telegram_message_cleaner.py -s 1210787553 1274948231

    +------------+---------------+----------+
    |     ID     |     Group     | Messages |
    +------------+---------------+----------+
    | 1210787553 | Bob and Alice | 75       |
    | 1274948231 |    Project    | 68       |
    +------------+---------------+----------+

4.Delete messages from 'Bob and Alice' chat:

    ./telegram_message_cleaner.py -d 1210787553

5.Delete messages from 'Bob and Alice', 'Project' chats:

    ./telegram_message_cleaner.py -d 1210787553 1274948231
```


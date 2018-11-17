import argparse
import asyncio
import sys

from prettytable import PrettyTable
from telethon import TelegramClient

# Use your own values here
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'
client = TelegramClient('Telegram Message Cleaner', api_id, api_hash)


async def get_info(chat):

    messages = (
        await client.get_messages(chat.entity, limit=None, from_user='me') if hasattr(chat, 'entity')
        else await client.get_messages(chat, limit=None, from_user='me')
    )

    id_ = chat.id
    name = chat.title
    total_messages = messages.total
    return id_, name, total_messages


async def group_messages_statistic(ids):

    info = []
    await client.start()

    dialogs = await client.get_dialogs()
    groups = (
        [await client.get_entity(int(dialog_id)) for dialog_id in ids] if ids
        else [dialog for dialog in dialogs if dialog.is_group]
    )

    for future in asyncio.as_completed(map(get_info, groups)):
        id_, name, total_messages = await asyncio.shield(future)
        info.append((str(id_).lstrip("-"), name, total_messages))

    return info


def get_group_messages_statistic(ids):

    loop = asyncio.get_event_loop()
    stats = loop.run_until_complete(group_messages_statistic(ids))

    table = PrettyTable()
    table.field_names = ['ID', 'Group', 'Messages']
    table.align['ID'] = 'c'
    table.align['Group'] = 'c'
    table.align['Messages'] = 'l'
    table.sortby = 'Messages'
    table.reversesort = True

    for group in stats:
        if group[2] == 0:
            continue
        table.add_row(list(group))

    print(table)


async def delete_messages(ids):

    await client.start()
    await client.get_dialogs()

    for id_ in ids:
        chat = await client.get_entity(int(id_))
        messages = await client.get_messages(chat, limit=None, from_user='me')

        for message in messages:
            await message.delete()


def delete(ids):

    loop = asyncio.get_event_loop()
    loop.run_until_complete(delete_messages(ids))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        usage='%(prog)s [-s [id id ...]] [-d [id id ...]]',
        description='Show stats for your messages in all/specified group chats\nor delete all your messages in specified group chat(-s).',
        epilog="""\
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

    ./telegram_message_cleaner.py -d 1210787553 1274948231""")
    parser.add_argument('-s', '--statistic', nargs='*', default=None,
                        metavar='id', help='if you do not specify ID as an argument, it will show stats of your messages for all group chats')
    parser.add_argument('-d', '--delete', nargs='*', default=None,
                        metavar='id', help='deletes all your messages from the specified group chat ID(-s)')

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    if args.statistic or args.statistic == []:
        get_group_messages_statistic(args.statistic)
    elif args.delete:
        delete(args.delete)

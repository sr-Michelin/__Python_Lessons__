from telethon import TelegramClient, sync, events
import time as ti
import datetime

api_id = '3549787'
api_hash = '5555ebd73d481398772c8ad1f46cb205'
client = TelegramClient('session_name', api_id, api_hash)
client.start()

user_parse = 'Mike_Shevchenko'
user_parse = 'Seneca_8'
print('Object:', user_parse)


while True:
    if str(client.get_entity(user_parse).status).startswith('UserStatusOnline'):
        with open('Tg_parse.txt', 'a') as f:
            message = client.get_entity(user_parse).status.expires
            message_ = f'Object {user_parse} is online; {message}'
            f.write('\n' + message_)
            print(message_)
            ti.sleep(1)

    else:
        with open('Tg_parse.txt', 'a') as f:
            message_ = f'Object {user_parse} is offline'
            f.write('\n' + message_)
            print(message_)
            ti.sleep(1)

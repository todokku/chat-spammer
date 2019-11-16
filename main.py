# -*- coding: utf-8 -*-

from telethon import TelegramClient, sync
import time
api_id = 1234567
api_hash = '123456789123456789123456879'

client = TelegramClient('pychat-spamer', api_id, api_hash)
client.start()
i = 0

print("""
                      __          __                                            
    ____  __  _______/ /_  ____ _/ /_      _________  ____ _____ ___  ___  _____
   / __ \/ / / / ___/ __ \/ __ `/ __/_____/ ___/ __ \/ __ `/ __ `__ \/ _ \/ ___/
  / /_/ / /_/ / /__/ / / / /_/ / /_/_____(__  ) /_/ / /_/ / / / / / /  __/ /    
 / .___/\__, /\___/_/ /_/\__,_/\__/     /____/ .___/\__,_/_/ /_/ /_/\___/_/     
/_/    /____/                               /_/                             v.0.01     """)

chat_name = input("Введите названия вашего чата: ")
users = client.get_participants(chat_name)
for user in users:
    if user.username is not None:
        global u_name
        u_name = user.username
        i += 1

print("Было найдено", i, "пользователей которым можно отправить сообщения.")
f = open('message.txt', 'r', encoding="utf-8")
print(text)

for user in users:
    if user.username is not None:
        u_name = user.username
        i += 1
        print(str(i) + "." + u_name)#
        #client.send_file(u_name, 'logo.jpg')
        client.send_message(u_name, text) 
        time.sleep(40)    
print("Было отправлено", i, "сообщений")



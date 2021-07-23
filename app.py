# Created by Scrippy. Also known as ScriptIntelligence, Scrizeebe, and Script404
# Started Jul. 22, 2021

print(('-' * 23) + '\nTest build of Szeebe.py\nCreated by: Scrippy\nStarted Jul. 22, 2021\n' + ('-' * 23))

is_Active = True

if is_Active:
    print('Szeebe is able to run.\n' + ('-' * 23))
else:
    print('Szeebe is unable to run.\n' + ('-' * 23))
    quit()

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX')

import discord

class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged in as...')
            print(self.user.name)
            print(self.user.id)
            print('-' * 23)

        async def on_message(self, message):
            if message.author.id == self.user.id:
                return

            if message.content.lower() == 'hi':
                await message.channel.send('Hello there')
                return
            if message.content.lower() == 'hello there':
                await message.channel.send('General Kenobi')
                return

            if message.content.lower() == 'general kenobi':
                await message.channel.send('You are a bold one')


client = MyClient()
client.run(TOKEN)
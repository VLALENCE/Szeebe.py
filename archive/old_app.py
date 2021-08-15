# Created by Scrippy. Also known as ScriptIntelligence, Scrizeebe, and Script404
# Started Jul. 22, 2021
# Version Finished Jul. 25, 2021

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

import math

from datetime import datetime
import time

start_time = time.time()

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
                return

            if message.content.lower() == 'test':
                await message.channel.send(message.created_at)
                return

            if message.content.lower() == PREFIX + 'ping':
                embed = discord.Embed(description='Pong! Response Time:\n'+str(round(client.latency, 3)) + ' Seconds (' + str(round(client.latency*1000)) + 'ms)!', color=0x00ff5f, timestamp=datetime.utcnow())
                embed.set_author(name=self.user.name+' ⋅ Ping', icon_url=self.user.avatar_url)
                embed.set_footer(text=message.guild.name, icon_url=message.guild.icon_url)
                await message.channel.send(embed=embed)
                return

            if message.content.lower() == PREFIX + 'uptime':
                current_uptime = time.time()
                elapsed = current_uptime - start_time
                print(elapsed)
                days = str(round(elapsed / 86400))
                hours = str(round((elapsed / 3600) % 24))
                minutes = str(round((elapsed / 60) % 60))
                seconds = str(round((elapsed / 1) % 60))
                embed = discord.Embed(description=days+' days, '+hours+' hours, '+minutes+' minutes, '+seconds+' seconds.', color=0x00ff5f, timestamp=datetime.utcnow())
                embed.set_author(name=self.user.name + ' ⋅ Uptime', icon_url=self.user.avatar_url)
                embed.set_footer(text=message.guild.name, icon_url=message.guild.icon_url)
                await message.channel.send(embed=embed)
                return

client = MyClient()
client.run(TOKEN)
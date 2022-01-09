# By ScriptIntelligence
# Started Aug. 14, 2021

# // Libraries
import asyncio
import discord
import io
import aiohttp
import os

from discord import activity
from asyncio import sleep
from lib.bot.env_variables import prefix


# // Variables

# // Functions
#async def my_background_task(self):
    #while not discord.is_closed:
        #activity = discord.Activity(type=self.ActivityType.listening, name=prefix+'help | '+len(list(self.guilds)))
        #self.change_presence(status=self.Status.online, activity=activity)
        #asyncio.sleep(10)
        #activityagain = self.Activity(type=self.ActivityType.listening, name=prefix+'help | '+ len(list(self.users)))
        #self.change_presence(status=self.Status.online, activity=activityagain)
        #asyncio.sleep(10)

async def status_task(self):
    while True:
        activity = discord.Activity(type=discord.ActivityType.listening, name=('s>help | '+ str(len(list(self.guilds)))+' servers!'))
        await self.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(10)
        activity = discord.Activity(type=discord.ActivityType.listening, name=('s>help | [Broken] '+ str(len(list(self.users)))+' users!'))
        await self.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(10)
        activity = discord.Activity(type=discord.ActivityType.listening, name=('s>help | Running in Python! [Demo]'))
        await self.change_presence(status=discord.Status.online, activity=activity)
        await asyncio.sleep(10)

#def createTriggerWordResponse(message):
#    if message.content.lower() == 'hi': return message.channel.send('Hello there')
#    if message.content.lower() == 'hello there': return message.channel.send('General Kenobi')
#    if message.content.lower() == 'general kenobi': return message.channel.send('You are a bold one')
#    if message.content.lower().find('birthday') >= 0: return message.channel.send('Happy Birthday!!!')
#    if message.content.lower().find('scrizeebe') >= 0: return message.channel.send('Script*')
#    if message.content.lower().find('boing') >= 0: return message.channel.send('boing')
#    if message.content.lower().find('frog') >= 0: return message.channel.send('boing ribbit boing')
#    if message.content.lower() == 'no.': return message.channel.send(files=discord.File('https://github.com/Scrippy/conch.rbx/raw/main/Audio/no.mp3'))
#    if message.content.lower() == 'nothing.': return
#    if message.content.lower() == 'try asking again.': return
#    if message.content.lower() == 'i dont think so': return
#    if message.content.lower() == 'i don\' think so': return
#    if message.content.lower() == 'maybe some day.': return
#    if message.content.lower() == 'yes.': return


def createTriggerWordResponse(message):
    normalResponseFiles = os.listdir(r"lib\bot\responses\normal")
    for file in normalResponseFiles:
        if file.endswith('.py'):
            responseFileName = file.split('.py')
            if message.content.lower() == responseFileName[0]:
                return message.channel.send(responseFileName[0])

    wildcardResponseFiles = os.listdir(r"lib\bot\responses\wildcard")
    for file in wildcardResponseFiles:
        if file.endswith('.py'):
            responseFileName = file.split('.py')
            if message.content.lower().find(responseFileName[0]) >= 0: 
                return message.channel.send(responseFileName[0])
    return

def createClientReadyResponse(self):
    print(('-' * 23) + '\nLogged in as...\n' + self.user.name + '\n' + str(self.user.id) + '\n' + ('-' * 23))
    #self.loop.create_task(my_background_task(self))
    self.loop.create_task(status_task(self))
    return

def getCommandArgs(message):
    commandSplit = message.content.split('>')
    commandArgs = commandSplit[1].split(' ')
    return commandArgs
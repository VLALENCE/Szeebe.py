# By ScriptIntelligence
# Started Aug. 14, 2021

# // Libraries
import discord
import io
import aiohttp

# // Variables

# // Functions
def createTriggerWordResponse(message):
    if message.content.lower() == 'hi': return message.channel.send('Hello there')
    if message.content.lower() == 'hello there': return message.channel.send('General Kenobi')
    if message.content.lower() == 'general kenobi': return message.channel.send('You are a bold one')
    if message.content.lower().find('birthday') >= 0: return message.channel.send('Happy Birthday!!!')
    if message.content.lower().find('scrizeebe') >= 0: return message.channel.send('Script*')
    if message.content.lower().find('boing') >= 0: return message.channel.send('boing')
    if message.content.lower().find('frog') >= 0: return message.channel.send('boing ribbit boing')

    #if message.content.lower() == 'no.': return message.channel.send(files=discord.File('https://github.com/Scrippy/conch.rbx/raw/main/Audio/no.mp3'))
    #if message.content.lower() == 'nothing.': return
    #if message.content.lower() == 'try asking again.': return
    #if message.content.lower() == 'i dont think so': return
    #if message.content.lower() == 'i don\' think so': return
    #if message.content.lower() == 'maybe some day.': return
    #if message.content.lower() == 'yes.': return


def createClientReadyResponse(self):
    return print(('-' * 23) + '\nLogged in as...\n' + self.user.name + '\n' + str(self.user.id) + '\n' + ('-' * 23))

def getCommandArgs(message):
    commandSplit = message.content.split('>')
    commandArgs = commandSplit[1].split(' ')
    return commandArgs
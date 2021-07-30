# By ScriptIntelligence
# Started Jul. 25, 2021

# // Libraries
import discord
import io
import aiohttp

# // Variables

class check:

    def isTriggerWord(message):

        if message.content.lower() == 'hi': return True
        if message.content.lower() == 'hello there': return True
        if message.content.lower() == 'general kenobi': return True
        if message.content.lower().find('birthday') >= 0: return True
        if message.content.lower().find('scrizeebe') >= 0: return True
        if message.content.lower() == 'boing': return True
        if message.content.lower() == 'no.': return True
        if message.content.lower() == 'nothing.': return True
        if message.content.lower() == 'try asking again.': return True
        if message.content.lower() == 'i dont think so': return True
        if message.content.lower() == 'i don\' think so': return True
        if message.content.lower() == 'maybe some day.': return True
        if message.content.lower() == 'yes.': return True

    def isAuthorSelf(self, message):
        if message.author.id == self.user.id: return True

class do:

    def createTriggerWordResponse(message):
        if message.content.lower() == 'hi': return message.channel.send('Hello there')
        if message.content.lower() == 'hello there': return message.channel.send('General Kenobi')
        if message.content.lower() == 'general kenobi': return message.channel.send('You are a bold one')
        if message.content.lower().find('birthday') >= 0: return message.channel.send('Happy Birthday!!!')
        if message.content.lower().find('scrizeebe') >= 0: return message.channel.send('Script*')
        if message.content.lower() == 'boing': return message.channel.send('boing')

        if message.content.lower() == 'no.': return message.channel.send(files=discord.File('https://github.com/Scrippy/conch.rbx/raw/main/Audio/no.mp3'))
        #if message.content.lower() == 'nothing.': return
        #if message.content.lower() == 'try asking again.': return
        #if message.content.lower() == 'i dont think so': return
        #if message.content.lower() == 'i don\' think so': return
        #if message.content.lower() == 'maybe some day.': return
        #if message.content.lower() == 'yes.': return


    def createClientReadyResponse(self):
        return print(('-' * 23) + '\nLogged in as...\n' + self.user.name + '\n' + str(self.user.id) + '\n' + ('-' * 23))


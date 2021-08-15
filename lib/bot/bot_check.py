# By ScriptIntelligence
# Started Jul. 25, 2021

# // Libraries
import discord
import io
import aiohttp

# // Variables


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


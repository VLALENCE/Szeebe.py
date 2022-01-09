# By ScriptIntelligence
# Started Jul. 25, 2021

# // Libraries
import discord
import io
import aiohttp
import os
import runpy

# // Modules
from lib.bot import env_variables

# // Variables
TOKEN = env_variables.token()
PREFIX = env_variables.prefix()

#def isTriggerWord(message):
#    if message.content.lower() == 'hi': return True
#    if message.content.lower() == 'hello there': return True
#    if message.content.lower() == 'general kenobi': return True
#    if message.content.lower().find('birthday') >= 0: return True
#    if message.content.lower().find('scrizeebe') >= 0: return True
#    if message.content.lower().find('boing') >= 0: return True
#    if message.content.lower().find('frog') >= 0: return True
#    if message.content.lower() == 'no.': return True
#    if message.content.lower() == 'nothing.': return True
#    if message.content.lower() == 'try asking again.': return True
#    if message.content.lower() == 'i dont think so': return True
#    if message.content.lower() == 'i don\' think so': return True
#    if message.content.lower() == 'maybe some day.': return True
#    if message.content.lower() == 'yes.': return True

# Work In Progress
def isTriggerWord(message):
    normalResponseFiles = os.listdir(r"lib\bot\responses\normal")
    for file in normalResponseFiles:
        if file.endswith('.py'):
            responseFileName = file.split('.py')
            if message.content.lower() == responseFileName[0]: return True
    wildcardResponseFiles = os.listdir(r"lib\bot\responses\wildcard")
    for file in wildcardResponseFiles:
        if file.endswith('.py'):
            responseFileName = file.split('.py')
            if message.content.lower().find(responseFileName[0]) >= 0: return True
    return False
            


def isAuthorSelf(self, message):
    if message.author.id == self.user.id: return True

def isCommand(args):
    commandFiles = os.listdir(r"lib\bot\commands")
    for file in commandFiles:
        if file.endswith('.py'):
            print(file)
            commandFileName = file.split('.py')
            print(commandFileName[0])
            commandName = args[0]
            if commandName[0] == commandFileName[0]:
                print('isCommand ! ' + commandName[0])
                return True
    return False

def hasPrefix(message):
    if message.content.startswith(PREFIX): return True

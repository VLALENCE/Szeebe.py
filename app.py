# By ScriptIntelligence
# Started Jul. 25, 2021

# [Old] Structure Setup

# libraries
# modules
# settings
# events
# startup
# function

# [New] Structure Setup -- Drafting

# // app.py Script Initial -- Still TBD

# libraries
# modules
# ...

# // commands folder Script Initial

# class module
#      def __init__(self, args, command, user)
#           self.aliases = ['']
#           self.args = args
#           self.category = ''
#           self.command = command
#           self.cooldown = 0
#           self.name = ''
#           self.user = user
#
#      def execute(self)
#


# // Hierarchy

# .env
# .gitattributes
# .gitignore
# app.py
#   lib
#       bot
#           __init__.py
#           main.py
#
#       commands
#           __init__.py
#           avatar.py
#           commands.py
#           convert.py
#           help.py
#           info.py
#           ping.py
#           serverinfo.py
#           userinfo.py
#           uptime.py
# README.md

# // Libaries
import discord
import tracemalloc

# // Modules
from lib.bot import env_variables,bot_check,bot_do

# // Variables
TOKEN = env_variables.token()
PREFIX = env_variables.prefix()

# // Events
class myClient(discord.Client):
    async def on_ready(self):
        bot_do.createClientReadyResponse(self)

    async def on_message(self, message):
        if bot_check.isAuthorSelf(self, message): return

        #if bot_check.isTriggerWord(message):
            #await bot_do.createTriggerWordResponse(message)
            #return
        if bot_check.isCommand(message): return

# // Startup
tracemalloc.start()
client = myClient()
client.run(TOKEN)
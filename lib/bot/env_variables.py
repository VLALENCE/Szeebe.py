# By ScriptIntelligence
# Started Jul. 25, 2021

# // Libraries

# OS
import os

# .env Handling
from dotenv import load_dotenv

load_dotenv()

# // Variables

PREFIX = os.getenv('PREFIX')
TOKEN = os.getenv('TOKEN')

# // Module Functions

def prefix():
        return PREFIX

def token():
        return TOKEN
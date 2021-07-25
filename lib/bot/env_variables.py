# By ScriptIntelligence
# Started Jul. 25, 2021

# OS
import os

# .env Handling
from dotenv import load_dotenv

load_dotenv()

PREFIX = os.getenv('PREFIX')
TOKEN = os.getenv('TOKEN')

def prefix():
        return PREFIX

def token():
        return TOKEN
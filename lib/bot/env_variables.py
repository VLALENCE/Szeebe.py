# By ScriptIntelligence
# Started Jul. 25, 2021

# OS
import os

# .env Handling
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
PREFIX = os.getenv('PREFIX')

def prefix():
        return PREFIX

def token():
        return TOKEN
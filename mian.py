import json
import os
import random
import nextcord
from nextcord.ext import commands
bot = commands.Bot(command_prefix = '!', intents = nextcord.Intents.all())
prefix = '!'

with open('token.json', mode = 'r', encoding = 'utf8') as token:
    token_data = json.load(token)

# 連上線時的事件
@bot.event
async def on_ready():
    print(f'-> Logged in as {bot.user}!')

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')

if __name__ == '__main__':
    bot.run(token_data['token'])
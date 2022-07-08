from operator import ne
import nextcord
from nextcord.ext import commands
intents = nextcord.Intents.all()
client = commands.Bot(command_prefix = '/', intents = intents)

# 連上線時的事件
@client.event
async def on_ready():
    print(f'-> Logged in as {client.user}!')
    
@client.event
async def on_member_join(member):
    print(f'-> <@{member.id}> join {member.guild.name} server')

@client.event
async def on_member_remove(member):
    print(f'-> <@{member.id}> leave {member.guild.name} server')
    
client.run("OTkxMDQzMjY2Mjk0MjA2NDk0.GWwOKW.UEy-y0CvyeOWaaWKew7TUVIPk23qocH7ChND3c")
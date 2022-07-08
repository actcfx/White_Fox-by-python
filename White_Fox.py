from operator import ne
import nextcord
from nextcord.ext import commands
intents = nextcord.Intents.all()
client = commands.Bot(command_prefix = '/', intents = intents)

# 連上線時的事件
@client.event
async def on_ready():
    print(f'-> Logged in as {client.user}!')

#成員加入時的事件
@client.event
async def on_member_join(member):
    match(member.guild.id):
        case 991002551979737109:
            channel = client.get_channel(991020606587822181)
        case 875245594355068958:
            channel = client.get_channel(994376068293202101)
    await channel.send(f'歡迎 {member.mention} 加入{member.guild.name}伺服器，玩的開心！')
    print(f"-> {member} join '{member.guild.name}' server")

#成員離開時的事件
@client.event
async def on_member_remove(member):
    match(member.guild.id):
        case 991002551979737109:
            channel = client.get_channel(991020606587822181)
        case 875245594355068958:
            channel = client.get_channel(994376068293202101)
    await channel.send(f'{member.mention} 離開了{member.guild.name}伺服器，一路好走！')
    print(f"-> {member} leave '{member.guild.name}' server")

@client.event
async def on_message(msg):
    if msg.content[0] == '/':
        cmd = msg.content.strip('/')
    cmd = cmd.split(' ')

client.run("OTkxMDQzMjY2Mjk0MjA2NDk0.G_pnhZ.KVXQfButK8cRdDeUe5fjTffo98AE7AIcVXkjpc")
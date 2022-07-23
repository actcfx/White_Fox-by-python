import nextcord
from nextcord.ext import commands
import json
intents = nextcord.Intents.all()
client = commands.Bot(command_prefix='/', intents=intents)

with open ('token.json', mode = 'r', encoding='utf8') as token:
    token_data = json.load(token)

with open ('guildID.json', mode = 'r', encoding = 'utf8') as guildID:
    guildID_data = json.load(guildID)

with open ('channelID.json', mode = 'r', encoding = 'utf8') as channelID:
    channelID_data = json.load(channelID)

# 連上線時的事件
@client.event
async def on_ready():
    print(f'-> Logged in as {client.user}!')

# 成員加入時的事件
@client.event
async def on_member_join(member):
    if member.guild.id == guildID_data['測試bot用_ID']:
        channel = client.get_channel(channelID_data['wel_ch_ID_1'])
    elif member.guild.id == guildID_data['Nationalsozialistische-Deutschland_ID']:
        channel = client.get_channel(channelID_data['wel_ch_ID_2'])
    await channel.send(f'歡迎 {member.mention} 加入{member.guild.name}伺服器，玩的開心！')
    print(f"-> {member} join '{member.guild.name}' server")

# 成員離開時的事件
@client.event
async def on_member_remove(member):
    match(member.guild.id):
        case 991002551979737109:
            channel = client.get_channel(991020606587822181)
        case 875245594355068958:
            channel = client.get_channel(994376068293202101)
    await channel.send(f'{member.mention} 離開了{member.guild.name}伺服器，一路好走！')
    print(f"-> {member} leave '{member.guild.name}' server")

# 當有人發送訊息時的事件
@client.event
async def on_message(msg):
    if msg.author.bot:
        return
    match(msg.content):
        case 'wtf':
            await msg.channel.send('wtf')
            print(f"-> Send 'wtf' to {msg.channel.name}")
    if msg.channel.id == 992721929008066591 or msg.channel.id == 992026961494941726:
        if msg.content[0] == '/':
            cmd = msg.content.strip('/')
            cmd = cmd.split(' ')
            match(cmd[0]):
                case 'say':
                    if len(cmd) > 1:
                        await msg.channel.send(cmd[1])
                        print(f"-> Send '{cmd[1]}' to '{msg.channel.name}'")
                    else:
                        await msg.delete(delay=1)  # 延遲單位為秒
                        await msg.channel.send('hi', delete_after=1)
                        print(f"-> Send 'hi' to {msg.channel.name}")
                        print("-> Delete 'hi' form bot's reply")
                        print(f"-> Delete {msg.author}'s message")
                case '老婆':
                    if msg.author.id == 407881227270356994:
                        await msg.reply('嗨！')
                        print(f"-> Reply '嗨！' to {msg.author}")
                    else:
                        await msg.reply('你沒有老婆！')
                        print(f"-> Reply '你沒有老婆！' to {msg.author}")


client.run(token_data['token'])

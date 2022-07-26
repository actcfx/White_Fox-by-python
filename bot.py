import json
import random
import nextcord
from nextcord.ext import commands
intents = nextcord.Intents.all()
client = commands.Bot(intents = intents)

with open('../White_Fox-by-python/token.json', mode = 'r', encoding = 'utf8') as token:
    token_data = json.load(token)

# 連上線時的事件
@client.event
async def on_ready():
    print(f'-> Logged in as {client.user}!')

# 當有人發送訊息時的事件
@client.event
async def on_message(ctx):
    if ctx.author.bot:
        return
    match(ctx.content):
        case 'wtf':
            await ctx.channel.send('wtf')
            print(f"-> Send 'wtf' to {ctx.channel.name}")

    if ctx.channel.id == 992721929008066591 or ctx.channel.id == 992026961494941726 or ctx.channel.id == 1001198121952489623:
        if ctx.content[0] == '!':
            cmd = ctx.content.strip('!')
            cmd = cmd.split(' ')
            match(cmd[0]):
                case 'say':
                    if len(cmd) > 1:
                        await ctx.channel.send(cmd[1])
                        print(f"-> Send '{cmd[1]}' to '{ctx.channel.name}'")
                    else:
                        await ctx.delete(delay=1)  # 延遲單位為秒
                        await ctx.channel.send('hi', delete_after=1)
                        print(f"-> Send 'hi' to {ctx.channel.name}")
                        print("-> Delete 'hi' form bot's reply")
                        print(f"-> Delete {ctx.author}'s message")
                case '老婆':
                    if ctx.author.id == 407881227270356994:
                        await ctx.reply('嗨！')
                        print(f"-> Reply '嗨！' to {ctx.author}")
                    else:
                        await ctx.reply('你沒有老婆！')
                        print(f"-> Reply '你沒有老婆！' to {ctx.author}")
                case 'luck':
                    pic = luck()
                    await ctx.reply(file = pic)
                    print(f"-> Reply 'luck' to {ctx.author}")

def luck():
    rnd = random.randint(0, 5)
    pic = nextcord.File(f"../White_Fox-by-python/luck_image/luck_{rnd}.jpg")
    print(f"-> Luck successful! Rnd is {rnd}")
    return pic

client.run(token_data['token'])

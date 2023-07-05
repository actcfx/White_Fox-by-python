import os
import json
import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix = '!', intents = nextcord.Intents.all())
with open('token.json', mode = 'r', encoding = 'utf8') as token:
    token_data = json.load(token)


@bot.event
async def on_ready():
    print(f'---- Logged in as {bot.user}! ----')


@bot.command()
async def ping(ctx):    #ping cmd
    ping = round(bot.latency * 1000)
    await ctx.send(f'ping:{ping}ms')
    print(f'<-> {bot.user} ping is {ping}ms')


@bot.command()
@commands.is_owner()
async def load(ctx, extension):         #load
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'導入 {extension} 成功')
    print(f'✓ Loaded {extension} successful!')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):       #unload
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'導出 {extension} 成功')
    print(f'✓ Unloaded {extension} successful!')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):       #reload
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'重置 {extension} 成功')
    print(f'✓ Reloaded {extension} successful!')


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)
    print(f'<!> Catch message error: ```{error}```')


for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')

if __name__ == '__main__':
    bot.run(token_data['token'])
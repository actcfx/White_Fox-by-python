import json
import time
import random
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension


class Luck(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def luck(self, ctx):
        with open('luck.json', 'r', encoding = 'utf-8') as luck:
            luck_data = json.load(luck)
        now_time = time.strftime('%Y, %m, %d', time.localtime())

        if (luck_data[f'{ctx.author.name}'] == now_time):
            await ctx.reply('你已經測過今日運勢了，試圖改變運氣是不可能的唷！')
            print(f'<err> {ctx.author} already used !luck')
            return

        luck_data[f'{ctx.author.name}'] = now_time
        with open('luck.json', 'w', encoding = 'utf-8') as luck:
            json.dump(luck_data, luck, indent = 4, ensure_ascii = False)
        luck_random = random.randint(0, 5)
        luck_pic = nextcord.File(f"luck_image/luck_{luck_random}.jpg")
        await ctx.reply(file = luck_pic)
        print(f"<suc> {ctx.author}'s luck is {luck_random}")


def setup(bot):
    bot.add_cog(Luck(bot))
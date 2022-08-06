import nextcord
import random
from nextcord.ext import commands
from core.classes import Cog_Extension

class luck(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def luck(self, ctx):
        pic = _luck()
        await ctx.reply(file = pic)
        print(f"-> Reply 'luck' to {ctx.author}")

def _luck():
    rnd = random.randint(0, 5)
    pic = nextcord.File(f"../White_Fox-by-python/luck_image/luck_{rnd}.jpg")
    print(f"-> Luck successful! Rnd is {rnd}")
    return pic

def setup(bot):
    bot.add_cog(luck(bot))
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

class DD(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def DD(self, ctx):
        await ctx.reply(f"你是說<@300201809623121922>嗎")
        print(f"-> 黑糖#0525 is DD, DD斬首")

def setup(bot):
    bot.add_cog(DD(bot))
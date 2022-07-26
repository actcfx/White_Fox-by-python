import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

class ping(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"ping:{round(self.bot.latency*1000)}ms")
        print(f"-> {self.bot.user} ping is {round(self.bot.latency*1000)}ms")

def setup(bot):
    bot.add_ping(ping(bot))
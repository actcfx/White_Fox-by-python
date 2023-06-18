import time
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

routine = True


class Routine(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @commands.Cog.listener()
    def on_ready(self):
        while routine:
            now_hr = time.strftime("%h", time.localtime())



def setup(bot):
    bot.add_cog(Routine(bot))
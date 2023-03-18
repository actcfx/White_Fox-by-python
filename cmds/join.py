import json
import nextcord
import json
from nextcord.ext import commands
from core.classes import Cog_Extension

'''with open('../White_Fox-by-python/ID/guildID.json', mode = 'r', encoding = 'utf8') as guildID:
    guildID_data = json.load(guildID)
with open('../White_Fox-by-python/ID/channelID.json', mode = 'r', encoding = 'utf8') as channelID:
    channelID_data = json.load(channelID)'''

class Join(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 875245594355068958:
            await self.bot.get_channel(931852709114576957).send(f'hi {member.name}，好甲好甲')
            print(f'-> {member} join the server')


def setup(bot):
    bot.add_cog(Join(bot))
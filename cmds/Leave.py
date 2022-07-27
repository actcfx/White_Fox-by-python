import json
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

with open('../White_Fox-by-python/ID/guildID.json', mode = 'r', encoding = 'utf8') as guildID:
    guildID_data = json.load(guildID)
with open('../White_Fox-by-python/ID/channelID.json', mode = 'r', encoding = 'utf8') as channelID:
    channelID_data = json.load(channelID)

class Leave(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == guildID_data['測試bot用_ID']:
            channel = self.bot.get_channel(channelID_data['wel_ch_ID_1'])
        elif member.guild.id == guildID_data['Nationalsozialistische-Deutschland_ID']:
            channel = self.bot.get_channel(channelID_data['wel_ch_ID_2'])
        await channel.send(f'{member.mention} 離開了{member.guild.name}伺服器，一路好走！')
        print(f"-> {member} leave '{member.guild.name}' server")

def setup(bot):
    bot.add_cog(Leave(bot))
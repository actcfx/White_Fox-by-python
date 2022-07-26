import json
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

with open('../White_Fox-by-python/ID/guildID.json', mode = 'r', encoding = 'utf8') as guildID:
    guildID_data = json.load(guildID)
with open('../White_Fox-by-python/ID/channelID.json', mode = 'r', encoding = 'utf8') as channelID:
    channelID_data = json.load(channelID)

class Join(Cog_Extension):
    def __init__(self, client):
        self.client = client

    # 成員加入時的事件
    @commands.event
    async def on_member_join(self, member):
        if member.guild.id == guildID_data['測試bot用_ID']:
            channel = self.client.get_channel(channelID_data['wel_ch_ID_1'])
        elif member.guild.id == guildID_data['Nationalsozialistische-Deutschland_ID']:
            channel = self.client.get_channel(channelID_data['wel_ch_ID_2'])
        await channel.send(f'歡迎 {member.mention} 加入{member.guild.name}伺服器，玩的開心！')
        print(f"-> {member} join '{member.guild.name}' server")

def setup(client):
    client.add_cog(Join(client))
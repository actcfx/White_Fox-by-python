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
#        if member.guild.id == guildID_data['測試bot用_ID']:
        channel = self.bot.get_channel(978708780445495328)
#        elif member.guild.id == guildID_data['Nationalsozialistische-Deutschland_ID']:
#            channel = self.bot.get_channel(channelID_data['wel_ch_ID_2'])
        await channel.send(f'{member.mention} 歡迎～～\n可以透過 <#978708014695600188> 熟悉頻道功能\n歡迎到 <#987734120505421844> <#986372265820172299> 投稿\n如果想快速認識大家可以到 <#990553527547990046>\n啊還有我沒抽到阿晴，不要曬我:kokomi_sad:')
        print(f"-> {member} join '{member.guild.name}' server")


def setup(bot):
    bot.add_cog(Join(bot))
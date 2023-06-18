import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

WIFE_CHANNEL_ID = 1118725524974489770


class Old_Man(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @nextcord.slash_command(name="早安長輩圖", description="每日任務二")
    async def image(self, interaction: nextcord.Interaction):
        WIFE_CHANNEL = self.bot.get_channel(WIFE_CHANNEL_ID)
        try:
            await interaction.response.send_message("https://media.discordapp.net/attachments/1061199217923719240/1119262719279902750/1686923406759.jpg?width=686&height=686")
            print("<suc> 15號！老婆貓！")
        except Exception as err:
            await WIFE_CHANNEL.send(f"Catch error: {err}")
            print(f"<err> {err}")


def setup(bot):
    bot.add_cog(Old_Man(bot))

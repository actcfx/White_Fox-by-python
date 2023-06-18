import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

WIFE_CHANNEL_ID = 1118725524974489770


class Wife(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @nextcord.slash_command(name="每日關心賤臣的老婆畢業了沒", description="每日任務一")
    async def graduate(self, interaction: nextcord.Interaction):
        WIFE_CHANNEL = self.bot.get_channel(WIFE_CHANNEL_ID)
        try:
            await interaction.response.send_message("<@616997647231746106> 今天你老婆畢業了嗎")
            print("<suc> 人類們安安，我是瀕臨絕種團的十五號")
        except Exception as err:
            await WIFE_CHANNEL.send(f"Catch error: {err}")
            print(f"<err> {err}")


def setup(bot):
    bot.add_cog(Wife(bot))

import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension


class Delete_Message(Cog_Extension):

    @nextcord.slash_command(name="刪除訊息")
    async def clear(self, interaction: nextcord.Interaction, num: int = nextcord.SlashOption(name="刪除的訊息數", description="請輸入刪除的訊息數")):
        try:
            await interaction.channel.purge(limit=num)
            await interaction.response.send_message(f'已刪除 {num} 則訊息', ephemeral=True)
            print(f"<> Deleted {num} messages from #{interaction.channel.name}")

        except Exception as err:
            await interaction.channel.send(f"Purge slash_cmd catch error: ```{err}```")
            print(f">err< Purge slash_cmd: ```{err}```")


def setup(bot):
    bot.add_cog(Delete_Message(bot))

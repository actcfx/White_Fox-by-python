import time
import json
import random
import datetime
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

WIFE_CHANNEL_ID = 1118725524974489770


class Wife(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @nextcord.slash_command(name="每日關心賤臣的老婆畢業了沒", description="每日任務")
    async def graduate(self, interaction: nextcord.Interaction):
        try:
            with open("luck.json", "r", encoding="utf-8") as luck:
                luck_data = json.load(luck)
            with open("luck_img.json", "r", encoding="utf-8") as luck_img:
                luck_img_list = json.load(luck_img)
            WIFE_CHANNEL = self.bot.get_channel(WIFE_CHANNEL_ID)
            now_date = time.strftime('%Y/%m/%d', time.localtime())
            luck_random = random.randint(0, 5)  # random luck_img number

            embed = nextcord.Embed(description=f"{now_date} 簽到成功",
                                   color=nextcord.Colour.random(),
                                   timestamp=datetime.datetime.now())
            embed.set_author(name=f"{interaction.user.name}",
                             icon_url=f"{interaction.user.avatar}")
            embed.set_image(url=f"{luck_img_list[luck_random]}")

            try:
                if (luck_data[f'{interaction.user.id}'] == now_date):  # already signed in
                    await interaction.response.send_message("你今天已經提醒過賤臣囉", ephemeral=True)
                    print(f'>err< Wife slash_cmd: {interaction.user.name} already signed in')
                    return
            except:
                pass

            luck_data[f"{interaction.user.id}"] = now_date  # note down the sign date
            with open('luck.json', 'w', encoding='utf-8') as luck:  # write to json
                json.dump(luck_data, luck, indent=4, ensure_ascii=False)

            await interaction.response.send_message("<@616997647231746106> 今天你老婆畢業了嗎")
            await WIFE_CHANNEL.send("https://media.discordapp.net/attachments/1061199217923719240/1119262719279902750/1686923406759.jpg?width=686&height=686")
            await WIFE_CHANNEL.send(embed=embed)

            print(f"<> {interaction.user} 安安，我是瀕臨絕種團的十五號")

        except Exception as err:
            await WIFE_CHANNEL.send(f"Wife slash_cmd catch error: ```{err}```")
            print(f">err< Wife slash_cmd: ```{err}```")


def setup(bot):
    bot.add_cog(Wife(bot))

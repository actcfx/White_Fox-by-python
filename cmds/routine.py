import time
from datetime import datetime
import asyncio
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

routine = True
GRADUATE_DATE = datetime(2023, 6, 30)
WIFE_CHANNEL_ID = 1118725524974489770


class Routine(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            WIFE_CHANNEL = self.bot.get_channel(WIFE_CHANNEL_ID)
            while routine:
                now = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())  # get current time (date and time)
                now_hr = time.strftime("%H", time.localtime())  # get current time (only date)

                delta = GRADUATE_DATE - datetime.now()      # get delta time
                days, seconds = delta.days, delta.seconds   # convert seconds to days
                hours, seconds = divmod(seconds, 3600)      # convert seconds to hours
                minutes, seconds = divmod(seconds, 60)      # convert seconds to minutes
                delta_time = f"{days}天{hours}小時{minutes}分{seconds}秒"   # convert to str

                if now_hr == "08":
                    await WIFE_CHANNEL.send(f"現在是{now}，距離賤臣老婆畢業還有{delta_time}，記得提醒賤臣醒來！")
                    print(f"<>距離老婆貓畢業還有{delta_time}")
                await asyncio.sleep(3600)  # wait 1 hour

        except Exception as err:
            await WIFE_CHANNEL.send(f"Routine catch error: ```{err}```")
            print(f">err< Routine: ```{err}```")


def setup(bot):
    bot.add_cog(Routine(bot))

import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension
prefix = '!'

class say(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author.bot:
            return
    
        if ctx.content[0] == prefix:
            if ctx.channel.id == 992721929008066591 or ctx.channel.id == 992026961494941726 or ctx.channel.id == 1001198121952489623:
                cmd = ctx.content.strip(prefix)
                cmd = cmd.split(' ')
                if cmd[0] == 'say':
                    if len(cmd) > 1:
                        await ctx.channel.send(cmd[1])
                        print(f"-> Send '{cmd[1]}' to '{ctx.channel.name}'")
                    else:
                        await ctx.channel.send('hi')
                        print(f"-> Send 'hi' to {ctx.channel.name}")
        await self.bot.process_commands(ctx)

def setup(bot):
    bot.add_cog(say(bot))
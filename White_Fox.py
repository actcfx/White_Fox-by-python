from operator import ne
import nextcord
from nextcord.ext import commands
intents = nextcord.Intents.all()
client = commands.Bot(command_prefix = '/', intents = intents)

# 連上線時的事件
@client.event
async def on_ready():
    print(f"-> Logged in as {client.user}!")
    
client.run("OTkxMDQzMjY2Mjk0MjA2NDk0.Gm3I-r.BIsetmkLIJt4jVNYa3Mcbv_G09qRQFnDZzj4Mg")
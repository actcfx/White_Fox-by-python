import nextcord
from nextcord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self, client):
        self.client = client
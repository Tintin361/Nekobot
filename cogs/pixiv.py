from http import client
import discord
from discord.ext import commands
import passwords

class Pixiv(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        
        
def setup(bot):
    bot.add_cog(Pixiv(bot))
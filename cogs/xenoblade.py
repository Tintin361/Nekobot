from random import choice

import passwords as pswd
from discord.embeds import Embed
from discord.ext import commands
from pybooru import Danbooru

dan = Danbooru('danbooru', username="Kiri-chan27", api_key=pswd.danbooru_api)

class Xenoblade(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        
    @commands.command(name="nia", aliases=["Nia"])
    async def nia(self, ctx):
        await ctx.message.delete()
        # Petit message d'attente
        search_msg = await ctx.send("<a:search:944484192018903060> Recherche en cours...")
            
        try:
            message = from_danbooru("nia_(xenoblade)")
            await ctx.send(embed=message)
        except:
            await search_msg.edit(content="Erreur: la commande à plantée.")
            return
        await search_msg.delete()
        
        
    @commands.command(name="mio", aliases=["Mio"])
    async def mio(self, ctx):
        await ctx.message.delete()
        # Petit message d'attente
        search_msg = await ctx.send("<a:search:944484192018903060> Recherche en cours...")
            
        try:
            message = from_danbooru("mio_(xenoblade)")
            await ctx.send(embed=message)
        except:
            await search_msg.edit(content="Erreur: la commande à plantée.")
            return
        await search_msg.delete()
        
    
def from_danbooru(tag: str) -> Embed:
    color = 0x00314D
    
    posts = dan.post_list(tags=tag, limit=1000)
    post = choice(posts)
            
    # Envoie du message Embed
    neko = tag[:-12].capitalize()
    message = Embed(title=neko, description=f"", color=color)
    message.add_field(name="Lien:", value=post['file_url'], inline=True)
    message.set_footer(text=f"Depuis Danbooru- ID: {post['id']}", icon_url="https://avatars.githubusercontent.com/u/57931572?s=280&v=4")
            
    message.set_image(url=post['file_url'])
    
    
    return message
        

def setup(bot):
    bot.add_cog(Xenoblade(bot))

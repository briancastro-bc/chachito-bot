from typing import Tuple

from discord import Embed, Message, Colour
from discord.ext.commands import command, Cog, Bot, Context

class Messages(Cog):
    
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        
    @command(name='embedm')
    async def create_embed_message(self, ctx: Context, title: str=None, description: str=None):
        if title is None or description is None:
            await ctx.send('¿Qué debería poner en el mensaje?')
            return
        await ctx.send(embed=Embed(
            title=title, 
            type='rich', 
            description=description,
            colour=Colour.random()
        ))
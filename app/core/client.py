from typing import List

from discord import Message, HTTPException, Game, Status
from discord.ext.commands import Bot
from random import randrange

from .logger import Logger

class Chachito(Bot):
    
    def __init__(self, command_prefix, help_command=None, description=None, **options):
        super().__init__(command_prefix, help_command, description, **options)
    
    async def on_ready(self):
        print('Bot {0} connected # {1}'.format(self.user.name, self.user.id))
        Logger.start()
        game = Game('ser YouTuber')
        await self.change_presence(activity=game, status=Status.online)
    
    async def on_message(self, message: Message):
        if message.author.id == self.user.id:
            return
        if message.content.startswith('test'):
            def take_random_message(words_quantity: int=2):
                words_list: List[str] = ['amigo', 'cielo', 'mar', 'rio', 'bonito', 'playa']
                final_word: str = ""
                for i in range(words_quantity):
                    random = randrange(len(words_list))
                    final_word += f"{words_list[random]} "
                return final_word
            try:
                await message.reply(
                    f"I'm working, I going to send a random sentence: {take_random_message()}",
                    mention_author=True
                )
            except HTTPException:
                return
        await self.process_commands(message)
    
    async def on_error(self):
        pass
    
    async def on_disconnect(self):
        print('{0} was disconnected # {1}'.format(self.user.name, self.user.id))
from dotenv import load_dotenv

from discord.ext.commands import when_mentioned_or, HelpCommand

from core import Chachito, settings
from commands import Messages

def main():
    bot = Chachito(
        command_prefix=when_mentioned_or("$", "?", "!"),
        description='Chachito es el bot de nuestra comunidad',
    )
    # Adding bot commands
    bot.add_cog(Messages(bot))
    # Running bot
    bot.run(settings.CLIENT_DISCORD_TOKEN)

if __name__ == '__main__':
    load_dotenv()
    main()
import disnake, config
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    

def setup(bot):
    bot.add_cog(Owner(bot))
    print(f"> Extension {__name__} is ready")
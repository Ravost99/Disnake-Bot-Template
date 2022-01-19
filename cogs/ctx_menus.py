import disnake, config
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command


class Ctx_Menus(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    # a simple user / context menu command
    


def setup(bot):
    bot.add_cog(Ctx_Menus(bot))
    print(f"> Extension {__name__} is ready")
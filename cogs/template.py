import disnake, config
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command


class Template(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    # a slash command, add a custom name and description
    @slash_command(
      name="testcommand",
      description=None#add your description here
    )
    async def testcommand(self, inter):
        # remember to remove the 'pass' and add your own stuff here
        pass


def setup(bot):
    bot.add_cog(Template(bot))
    print(f"> Extension {__name__} is ready")
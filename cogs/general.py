import disnake, config
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command


class General(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @slash_command(
      name="ping",
      description="Check if the bot is alive"
    )
    async def ping(self, inter):
        embed = disnake.Embed(
          title=":ping-pong: Pong!",
          description="I'm alive!",
          color=disnake.Color.green()
        )
        await inter.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))
    print(f"> Extension {__name__} is ready")
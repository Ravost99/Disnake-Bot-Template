import disnake, config
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command


class Ctx_Menus(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @user_command(name="BotInfo")
    async def BotInfo(self, inter):
        embed = disnake.Embed(
          title=f"Name: {self.bot.user}",
          description=f"ID: {self.bot.user.id}",
          color=disnake.Color.green()
        )
        embed.add_field(
          name="Owner information",
          value="Ravost99#3361"
        )
        embed.add_field(
          name="Disnake Version",
          value=f"{disnake.__version__}"
        )
        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        await inter.response.send_message(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Ctx_Menus(bot))
    print(f"> Extension {__name__} is ready")
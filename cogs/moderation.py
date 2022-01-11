import disnake, config
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    #optional permissions remove if you dont want it
    @commands.has_permissions(manage_nicknames=True)
    @slash_command(
      name="Nick",
      description="Change the nickname of a user"
    )
    async def nick(self, inter, member: disnake.User, *, nickname: str):
        try:
          await member.edit(nick=nickname)
          embed = disnake.Embed(
            title=":white_check_mark: Changed Nickname!",
            description=f"**{member}'s** new nickname is **{nickname}**!",
            color=config.success
          )
          await inter.send(embed=embed)
        except:
          embed = disnake.Embed(
            title="Error",
            description=f"An error occurred while trying to change the nickname of {member}",
            color=config.error
          )
          embed.add_field(
            name="Faq",
            value="Try making sure by role is higher than the user's role!"
          )
          await inter.send(embed=embed)

    @commands.has_permissions(manage_channels=True)
    @slash_command(
      name="lock",
      description="Lock a channel"
    )
    async def lock(self, inter, channel: disnake.TextChannel=None):
        channel = channel or inter.channel
        overwrite = channel.overwrites_for(inter.guild.default_role)
        overwrite.send_messages = False
        overwrite.add_reactions = False
        await channel.set_permissions(inter.guild.default_role, overwrite=overwrite)
        await channel.send(":lock: Channel Locked.")
    
    @commands.has_permissions(manage_messages=True)
    @slash_command(
      name="unlock",
      description="Unlock a channel"
    )
    async def unlock(self, inter, channel: disnake.TextChannel=None):
        channel = channel or inter.channel
        overwrite = channel.overwrites_for(inter.guild.default_role)
        overwrite.send_messages = True
        overwrite.add_reactions = True
        await channel.set_permissions(inter.guild.default_role, overwrite=overwrite)
        await channel.send(":unlock: Channel Unlocked.")



def setup(bot):
    bot.add_cog(Moderation(bot))
    print(f"> Extension {__name__} is ready")
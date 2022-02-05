import disnake, config
from disnake.ext import commands
from disnake.ext.commands import slash_command, user_command, message_command

#===NOTICE===
# i would recommend making a role
# with all permissions for admin to run these commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    #optional permissions remove if you dont want it
    @commands.has_permissions(manage_nicknames=True)
    @slash_command(
      name="nick",
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

    @commands.has_permissions(kick_members=True)
    @slash_command(
      name="kick",
      description="Kick a member from a server"
    )
    async def kick(self, inter, member: disnake.User, *, reason: str = "Not specified"):
      await member.kick(reason=reason)
      embed = disnake.Embed(
        title=f"{member} was kicked by {inter.author}",
        description=reason,
        color=config.success
      )
      await inter.send(embed=embed)

    @commands.has_permissions(ban_members=True)
    @slash_command(
      name="ban",
      description="Ban a user from a server and all messages after days"
    )
    async def ban(self, inter, member: disnake.Member, delete_msg_days: int, *, reason: str = None):
      if delete_msg_days > 7: #can only delete messages less than 7 days
        delete_msg_days = 7
      await member.ban(delete_message_days=delete_msg_days, reason=reason)
      embed = disnake.Embed(
        title=f"{member} was banned by {inter.author}",
        description=f"Reason: {reason}",
        color=config.success
      )
      await inter.send(embed=embed)
    
    @commands.has_permissions(administrator=True)
    @slash_command(
      name="unban",
      description="Unban a user, use the user's id"
    )
    async def unban(self, inter, member_id, *, reason: str):
      member_id = int(member_id)
      member = await self.bot.fetch_user(member_id)
      await inter.guild.unban(member, reason=reason)
      embed = disnake.Embed(
        title=f"{member} was unbanned by {inter.author}",
        description=f"Reason: {reason}",
        color=config.success
      )
      await inter.send(embed=embed)

    @commands.has_permissions(administrator=True)
    @slash_command(
      name="move",
      description="Move the member to a voice channel"
    )
    async def move(self, inter, member: disnake.User, channel: disnake.VoiceChannel = None):
      if member.voice:
        await member.edit(voice_channel=channel)
        embed = disnake.Embed(
          title="Moved!",
          description=f"{member} was moved to {channel}",
          color=config.success
        )
        await inter.send(embed=embed)
      else:
        embed = disnake.Embed(
          title="Error!",
          description=f"{member} is not connected to a voice channel!",
          color=config.error
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

    @commands.has_permissions(manage_channels=True)
    @slash_command(
      name="archive",
      description="Archive a channel, voice channel or stage channel"
    )
    async def archive(self, inter, channel: disnake.TextChannel = None, voice_channel: disnake.VoiceChannel = None, stage_channel: disnake.StageChannel = None):
      channel = channel or voice_channel or stage_channel

      overwrite = channel.overwrites_for(inter.guild.default_role)
      overwrite.send_messages = False
      overwrite.add_reactions = False
      category = disnake.utils.get(inter.guild.channels, id=config.archive_id)

      embed = disnake.Embed(
        title=":white_check_mark: Archived!",
        color=config.success
      )
      await inter.send(embed=embed)
      await channel.edit(category=category)


def setup(bot):
    bot.add_cog(Moderation(bot))
    print(f"> Extension {__name__} is ready")
import typing

import discord
from discord import app_commands, Interaction, Member, TextInput, permissions
from discord import Permissions
from discord.ext import commands

class ban(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name='ban', description="Ban a user")
    #defoult perm
    async def ban(self, interaction: discord.Interaction,
                  user: Member, reason: str = None):
        if user.guild_permissions.administrator:
            await interaction.response.send_message("You can't ban an admin =((")
        elif user.id == interaction.user.id:
            await interaction.response.send_message("You can't ban yourself")
        elif not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("You can't ban bacause you are not an admin =((")
        else:
            if reason == None:
                reason = "no reason"
            await user.ban(reason=reason)
            await interaction.response.send_message(f'Banned user {user.mention} for {reason}')

async def setup(client: commands.Bot) -> None:
    await client.add_cog(ban(client))
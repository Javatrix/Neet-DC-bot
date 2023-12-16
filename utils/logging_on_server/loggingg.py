import json
import os
import typing
import discord
from discord import app_commands, Interaction, Member, TextInput, permissions
from discord import Permissions
from discord.ext import commands

class Logs():

    def __init__(self, client: commands.Bot, server, message):
        self.client = client
        self.server = server
        self.message = message

    def get_channel(self):
        serwers = []
        for file in os.listdir(".../servers"):
            serwers.append(file)
        if self.server in serwers:
            file_path = ".../servers/" + self.server + 'config.json'
            with open(file_path, 'r') as config_file:
                info = json.load(config_file)
            channel_id = info["logs_chat"]
            return channel_id
        else:
            return None

    async def sent_log(self, interaction: discord.Interaction):
        channel_id = self.get_channel(self)
        if channel_id != None:
            channel = self.get_channel(channel_id)
            await channel.send(self.message)

async def setup(self, server, message):
    await Logs.__init__(self, server, message)
    await Logs.sent_log()
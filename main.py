'''
    NEOdrew discord bot. Created by thirdoul.
'''

# Discord-related libraries
import discord
from discord import app_commands

# Base libraries
import time
import datetime
import random

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name='ping', description='ping pong', guild=discord.Object(id=587471529118531595))
async def ping(interaction):
    await interaction.response.send_message("pong!")

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=587471529118531595))
    print(f"Client ready!")

client.run('ODM1NzQwMzMwMTExOTI2MzEy.GX1Dgn.tmBv3cIUA8TpV1znZaws9dipy8hwDZjgEJvfPg')

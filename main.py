'''
    NEOdrew discord bot. Created by thirdoul.
    -------------------------------------------    

    This bot was originally designed for the Artism(Surreal) discord server and its partners, however the code will remain open to anyone who wants to use and/or modify it.

'''

# Discord-related libraries
import discord
from discord import app_commands
from discord.ext import commands

# Base libraries
import time
import datetime
import random

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


class Partners:
    artism = 587471529118531595
    omescape = 1039442477079347261

# Command for testing. Will respond with 'pong' on use.
@tree.command(name='ping', description='ping pong', guild=discord.Object(id=Partners.artism))
async def ping(interaction):
    await interaction.response.send_message("pong!")


# Drew commands




# All help commands
@tree.command()
async def help(interaction):
    await interaction.response.send_message("help command!")

group = app_commands.Group(name='help', description='View helpfull command information!')

@group.command()
async def ping(interaction):
    await interaction.response.send_message("command for debugging. should reply with 'pong'")

tree.add_command(group, guild=discord.Object(id=Partners.artism))




# On bot startup
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=Partners.artism))
    print(f"Client ready!")


client.run('ODM1NzQwMzMwMTExOTI2MzEy.Gk2Wr0.ZrLVLLA3UdFHrvWqKf_OzTPGM5fj1fH7Glunk8')

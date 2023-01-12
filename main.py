'''
    NEOdrew discord bot. Created by thirdoul.
    -------------------------------------------    

    This bot was originally designed for the Artism(Surreal) discord server and its partners, however the code will remain open to anyone who wants to use and/or modify it.

'''

# Discord-related libraries
import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import get

# Base libraries
import time
import datetime
import random


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


class Partners:
    def add(self):
        return discord.Object(id=self)

    artism = 587471529118531595
    omescape = 1039442477079347261


# Command for testing. Will respond with 'pong' on use.
@tree.command(name='ping', description='ping pong', guild=Partners.add(Partners.artism))
async def ping(interaction):
    await interaction.response.send_message("pong!")


# Drew commands
@tree.command(name='poll', description='Start a new poll. Up and down vote reactions will be automatically added.', guild=Partners.add(Partners.artism))
async def poll(interaction, *, question: str):
    start = time.time()
    await interaction.response.send_message(f"`Public poll`")
    msg = await interaction.channel.send(f'> {question}')
    reactions = ['<a:upvote:837521121447510018>', '<a:downvote:837517888420053003>']
    for emoji in reactions:
        await msg.add_reaction(emoji)


# All help commands
@tree.command()
async def help_commands(interaction):
    await interaction.response.send_message("help command!")

help = app_commands.Group(name='help', description='View helpfull command information!')

@help.command()
async def ping(interaction):
    await interaction.response.send_message("command for debugging. should reply with 'pong'")

tree.add_command(help, guild=discord.Object(id=Partners.artism))




# On bot startup
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=Partners.artism))
    print(f"Client ready!")


client.run('ODM1NzQwMzMwMTExOTI2MzEy.Gk2Wr0.ZrLVLLA3UdFHrvWqKf_OzTPGM5fj1fH7Glunk8')

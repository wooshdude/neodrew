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

# Flask libraries
from flask import Flask, redirect, render_template, flash, app

# Base libraries
import time
from datetime import datetime, date
import random


intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


class Partners:
    def add(self):
        return discord.Object(id=self)

    artism = 587471529118531595
    omescape = 1039442477079347261


# Command for testing. Will respond with 'pong' on use.
@tree.command(name='ping', description='ping pong')
async def ping(interaction):
    await interaction.response.send_message("pong!")


# Drew commands
@tree.command(name='poll', description='Start a new poll. Up and down vote reactions will be automatically added.')
async def poll(interaction, *, question: str):
    start = time.time()
    await interaction.response.send_message(f"`Public poll`")
    msg = await interaction.channel.send(f'> {question}')
    reactions = ['<a:upvote:837521121447510018>', '<a:downvote:837517888420053003>']
    for emoji in reactions:
        await msg.add_reaction(emoji)


@tree.command(name='roles', description='Summon a role selector.', guild=Partners.add(Partners.artism))
async def roles(interaction):
    await interaction.response.send_message("Select a role.", view=RoleSelectView(), ephemeral=True)
    

@tree.command(name='nick', description="Change someone's nickname.")
async def nick(interaction, member: discord.Member, *, nickname: str):
    await member.edit(nick=nickname)
    await interaction.response.send_message(f'nickname was changed for {member.mention} ')


# Buttons and menus
class RoleSelect(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Destiny 2",description="For all things that game."),
            discord.SelectOption(label="Minecraft",description="Access to the Minecraft server"),
            discord.SelectOption(label="Overwatch",description="winton")
            ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Destiny 2":
            role = interaction.guild.get_role(587473995155374111)
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Aquired new role <@&587473995155374111>", ephemeral=True)
        elif self.values[0] == "Option 2":
            role = interaction.guild.get_role(728352636713173002)
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Aquired new role <@&728352636713173002>", ephemeral=True)
        elif self.values[0] == "Option 3":
            role = interaction.guild.get_role(1026888371710214154)
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Aquired new role <@&1026888371710214154>", ephemeral=True)

class RoleSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(RoleSelect())


# All help commands
@tree.command()
async def help_commands(interaction):
    await interaction.response.send_message("help command!")

help = app_commands.Group(name='help', description='View helpfull command information!')

@help.command()
async def ping(interaction):
    await interaction.response.send_message("command for debugging. should reply with 'pong'")

tree.add_command(help, guild=discord.Object(id=Partners.artism))

current_guild = None

# On message
@client.event
async def on_message(interaction):
    today = date.today()
    now = datetime.now()
    global current_guild
    if current_guild != interaction.author.guild:
        current_guild = interaction.author.guild
        print(f'{current_guild}:')
    print(f'[({now}) {interaction.author.name} in {interaction.channel.name}] {interaction.content}')


# On bot startup
@client.event
async def on_ready():
    await tree.sync()
    print(f"Client ready!")

with open('../token.txt', 'r') as token:
    client.run(token.read())

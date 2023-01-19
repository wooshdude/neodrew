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
import requests


intents = discord.Intents.all()
client = discord.Client(intents=intents, help_command=None)
tree = app_commands.CommandTree(client)

class Partners:
    def add(self):
        return discord.Object(id=self)

    artism = 587471529118531595
    omescape = 1039442477079347261


# Command for testing. Will respond with 'pong' on use.
@tree.command(name='ping', description='ping pong')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong!")


# Drew commands
@tree.command(name='poll', description='Start a new poll. Up and down vote reactions will be automatically added.')
async def poll(interaction: discord.Interaction, *, question: str):
    start = time.time()
    await interaction.response.send_message(f"`Public poll`")
    msg = await interaction.channel.send(f'> {question}')
    reactions = ['<a:upvote:837521121447510018>', '<a:downvote:837517888420053003>']
    for emoji in reactions:
        await msg.add_reaction(emoji)


@tree.command(name='roles', description='Summon a role selector.', guild=Partners.add(Partners.artism))
async def roles(interaction: discord.Interaction):
    await interaction.response.send_message("Select a role.", view=RoleSelectView(), ephemeral=True)
    

@tree.command(name='nick', description="Change someone's nickname.")
async def nick(interaction: discord.Interaction, member: discord.Member, *, nickname: str):
    await member.edit(nick=nickname)
    await interaction.response.send_message(f'nickname was changed for {member.mention} ')


@tree.command(name='event', description="Start a new event that people can join")
async def event(interaction: discord.Interaction, code: str):
    request = requests.get(f"http://127.0.0.1/events/{code}")
    data = request.json()
    
    new_event = LfgPost(data, interaction)
    view = LfgButtons(new_event)
    await interaction.response.send_message(embed=new_event.get_embed(), view=view)


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
        elif self.values[0] == "Minecraft":
            role = interaction.guild.get_role(728352636713173002)
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Aquired new role <@&728352636713173002>", ephemeral=True)
        elif self.values[0] == "Overwatch":
            role = interaction.guild.get_role(1026888371710214154)
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"Aquired new role <@&1026888371710214154>", ephemeral=True)

class RoleSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(RoleSelect())


class LfgSelect(discord.ui.Select):
    def __init__(self, lfg_obj):
        options = [discord.SelectOption(label="Increase players", description="Use this to increase the needed players by 1."),
            discord.SelectOption(label="Decrease players", description="Use this to decrease the needed players by 1"),
            discord.SelectOption(label="End event", description="Ends the current event and deletes the message")]

        self.lfg_obj = lfg_obj

        super().__init__(placeholder="Event Options", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.id == self.lfg_obj.owner:
            if self.values[0] == "Increase players":
                self.lfg_obj.num_players += 1
                self.lfg_obj.update()
                await interaction.response.edit_message(embed=self.lfg_obj.get_embed())
            elif self.values[0] == "Decrease players":
                self.lfg_obj.num_players -= 1
                self.lfg_obj.update()
                await interaction.response.edit_message(embed=self.lfg_obj.get_embed())
            elif self.values[0] == "End event":
                em = discord.Embed(title='Event has ended!', description='This event has ended. Thanks for coming!')
                await interaction.response.edit_message(embed=em, view=None)
        else:
            await interaction.response.send_message("You are not the owner of this event!", ephemeral=True)


class LfgButtons(discord.ui.View):
    def __init__(self, lfg_obj):
        super().__init__(timeout=None)
        self.lfg_obj = lfg_obj
        self.add_item(LfgSelect(self.lfg_obj))

    @discord.ui.button(label="Join", style=discord.ButtonStyle.green)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.name not in self.lfg_obj.players:
            self.lfg_obj.players.append(interaction.user.name)
            self.lfg_obj.update()

            if int(self.lfg_obj.num_players) - len(self.lfg_obj.players) + 1 == 0:
                button.disabled = True
                await interaction.response.edit_message(embed=self.lfg_obj.get_embed(), view=self)
            else:
                await interaction.response.edit_message(embed=self.lfg_obj.get_embed())
        else:
            await interaction.response.send_message("You've already joined the event!", ephemeral=True)

    @discord.ui.button(label="Leave", style=discord.ButtonStyle.red)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.name in self.lfg_obj.players:
            self.lfg_obj.players.remove(interaction.user.name)
            self.lfg_obj.update()
            if int(self.lfg_obj.num_players) - len(self.lfg_obj.players) + 1 > 0:
                self.children[0].disabled = False
                await interaction.response.edit_message(embed=self.lfg_obj.get_embed(), view=self)
            else:
                await interaction.response.edit_message(embed=self.lfg_obj.get_embed())
        else:
            await interaction.response.send_message("You haven't joined the event!", ephemeral=True)


class LfgPost:
    def __init__(self, data, ctx):
        self.num_players = int(data['num'])
        self.ctx = ctx
        self.owner = ctx.user.id
        self.players = [ctx.user.name]

        self.title = data['title']
        self.description = data['event']
        self.em = None
            
        self.lst = []
        self.update()

    def update(self):
        self.em = discord.Embed(title=self.title, description=self.description)
        self.lst.clear()
        for i in range(self.num_players):
            if i < len(self.players):
                self.lst.append(self.players[i])
            else:
                self.lst.append('--------')
    
        self.em.add_field(name='Players', value='\n'.join(self.lst))

    def get_embed(self):
        return self.em


# All help commands
@tree.command()
async def help(interaction: discord.Interaction):
    em = discord.Embed(title='Help', description=f"Use /help <command> for more info.", color=0x1abc9c)

    em.add_field(name='Commands', value='poll\nnick\nroles')

    await interaction.response.send_message(embed=em)

help = app_commands.Group(name='help', description='View helpfull command information!')


@help.command()
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("command for debugging. should reply with 'pong'")


@help.command()
async def poll(interaction: discord.Interaction):
    em = discord.Embed(title='poll', description='Starts a poll. User and channel pings will still work.',
                       color=0x1abc9c)
    em.add_field(name='**Usage**', value=f'/poll <content>')
    em.add_field(name='Example', value=f'/poll example poll question')

    await interaction.response.send_message(embed=em)


@help.command()
async def nick(interaction: discord.Interaction):
    em = discord.Embed(title='nick', description='Allows users to edit nicknames', color=0x1abc9c)
    em.add_field(name='**Syntax**', value=f'/nick <@user> <nickname>')
    em.add_field(name='Example', value=f'/nick @example example nickname')

    await interaction.response.send_message(embed=em)


@help.command()
async def roles(interaction: discord.Interaction):
    em = discord.Embed(title='roles', description='Lets the user select their roles', color=0x1abc9c)
    em.add_field(name='**Syntax**', value=f'/roles')

    await interaction.response.send_message(embed=em)


tree.remove_command('help')
tree.add_command(help)


# On join
@client.event
async def on_member_join(member):
    role = member.guild.get_role(1036814232420892712)
    await member.add_roles(role)


# On message
current_guild = None

@client.event
async def on_message(interaction: discord.Interaction):
    today = date.today()
    now = datetime.now() 
    global current_guild
    if current_guild != interaction.author.guild:
        current_guild = interaction.author.guild
        print(f'{current_guild}:')
    print(f'[({now}) {interaction.author.name} in {interaction.channel.name}] {interaction.content}')

    if interaction.author.id != client.user.id:
        if 'penis' in interaction.content.casefold():
            await interaction.channel.send('penis')

        if 'i love' in interaction.content.casefold() and 'drew' in interaction.content.casefold():
            await interaction.channel.send(f'i love you too, {interaction.author.name}')

        if 'thank you' in interaction.content.casefold() and 'drew' in interaction.content.casefold():
            await interaction.channel.send(f"you're welcome, {interaction.author.name}")

        
# On bot startup
@client.event
async def on_ready():
    await tree.sync()
    print(f"Client ready!")

with open('../token.txt', 'r') as token:
    client.run(token.read())

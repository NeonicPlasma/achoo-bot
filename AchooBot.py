import discord
from discord.ext import commands

import random
import asyncio
import os

command_prefix='a/'
bot = commands.Bot(command_prefix)

game = discord.Game("killing Achoo")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=game)
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def storymessage(ctx, message, destination):
    author = ctx.message.author
    moderator = discord.utils.get(ctx.message.guild.roles, name='Moderator')
    if moderator in author.roles:
        channel = ctx.message.channel_mentions[0]
        await channel.send(message)
        
@bot.command()
async def roletest(ctx):
    author = ctx.message.author
    guild = ctx.message.guild
    moderator = discord.utils.get(guild.roles, name='Moderator')
    if moderator in author.roles:
        await guild.create_role(name="testing role")

@bot.command()
async def kill(ctx, person):
    author = ctx.message.author
    eliminated = discord.utils.get(ctx.message.guild.roles, name='Eliminated')
    alive = discord.utils.get(ctx.message.guild.roles, name='Currently Alive')
    if author.id == 194276511648448514:
        personMentioned = ctx.message.mentions[0]
        roles = personMentioned.roles
        if eliminated in roles:
            await ctx.send("This person is already eliminated!")
        else:
            if not alive in roles:
                await ctx.send("This person is not a contestant!")
            else:
                await ctx.send("Killed " + personMentioned.name + ". Rest in peace.")
                await personMentioned.add_roles(eliminated)
                await personMentioned.remove_roles(alive)
    else:
        await ctx.send("You have no permission to use this command.")

@bot.command()
async def status(ctx, mode):
    if mode == '1':
        await bot.change_presence(status=discord.Status.online, activity=game)
    elif mode == '2':
        await bot.change_presence(status=discord.Status.idle, activity=game)
    elif mode == '3':
        await bot.change_presence(status=discord.Status.dnd, activity=game)
    elif mode == '4':
        await bot.change_presence(status=discord.Status.invisible, activity=game)

bot.run(os.getenv('TOKEN'))

# https://discord.com/api/oauth2/authorize?client_id=1160302892729774190&permissions=139586750528&scope=bot

import discord
from discord.ext import commands
from discord import app_commands

import PIL.Image as Image
import numpy as np
import pixelmod

import os
from dotenv import load_dotenv


intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)
# TODO: real slash commands, not this ^

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("bye bye :c")
    await bot.close()



# @bot.command()
# async def poop(ctx):
#     print("pee!")
#     await ctx.send('pee!')

# TODO: need to sync commands to guild? how to properly do it... different when local testing vs deployed?
# technically only need to sync once...? can bot sync upon being added to server? how to resync while it's deployed (if even possible)?
# https://gist.github.com/AbstractUmbra/a9c188797ae194e592efe05fa129c57f
# https://discordpy.readthedocs.io/en/latest/interactions/api.html#discord.app_commands.CommandTree.copy_global_to

# @bot.command()
# async def sync(ctx):
#     guild = ctx.guild
#     bot.tree.copy_global_to(guild=guild) # this apparently just copies, still need to sync?

@bot.event
async def on_ready():
    await bot.tree.sync()


@bot.tree.command()
async def poop(interaction:discord.Interaction):
    print("pee!")
    await interaction.response.send_message("pee!", ephemeral=True)



##################################

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)

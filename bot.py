# https://discord.com/api/oauth2/authorize?client_id=1160302892729774190&permissions=139586750528&scope=bot

import discord
from discord.ext import commands

import PIL.Image as Image
import numpy as np
import pixelmod

intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("bye bye :c")
    await bot.close()



@bot.command()
async def poop(ctx):
    print("pee!")
    await ctx.send('pee!')

##################################
TOKEN = 'MTE2MDMwMjg5MjcyOTc3NDE5MA.Gh5Kre.P1OwCPqxx1deUh4Iyj9sMBOotEZX1gPNEAfgwU'
bot.run(TOKEN)
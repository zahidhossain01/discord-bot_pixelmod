# BOT NOTES:
# https://support-dev.discord.com/hc/en-us/articles/6381892888087-Bots-Buttons
# https://discord.com/blog/slash-commands-are-here

# command syncing notes for slash commands:
# https://gist.github.com/AbstractUmbra/a9c188797ae194e592efe05fa129c57f
# https://discordpy.readthedocs.io/en/latest/interactions/api.html#discord.app_commands.CommandTree.copy_global_to

# consider discord.js instead of discord.py some day?
# https://stackoverflow.com/questions/52241051/i-want-to-let-my-discord-bot-send-images-gifs

import discord
from discord.ext import commands

import PIL.Image as Image
import numpy as np
import pixelmod

import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.tree.sync()

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("bye bye :c")
    await bot.close()

@bot.tree.command()
async def poop(interaction:discord.Interaction):
    await interaction.response.send_message("pee!")

def create_image():
    # 100x100
    I = np.full((100,100,3), 128).astype(np.uint8)
    I[0:25,0:25,:] = 0
    I[75:100,75:100,:] = 255
    img = Image.fromarray(I)
    img.save("testimage.jpg", quality=95, subsampling=0)
    return "testimage.jpg"

@bot.command()
async def createimage(ctx):
    filepath = create_image()
    # await ctx.send(file=discord.File(filepath))
    with open(filepath, 'rb') as f:
        img = discord.File(f)
        await ctx.send(file=img)
    




##################################

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)

# FAQ: 
# https://discordpy.readthedocs.io/en/latest/faq.html

# BOT NOTES:
# https://support-dev.discord.com/hc/en-us/articles/6381892888087-Bots-Buttons
# https://discord.com/blog/slash-commands-are-here

# command syncing notes for slash commands:
# https://gist.github.com/AbstractUmbra/a9c188797ae194e592efe05fa129c57f
# https://discordpy.readthedocs.io/en/latest/interactions/api.html#discord.app_commands.CommandTree.copy_global_to

# https://stackoverflow.com/questions/52241051/i-want-to-let-my-discord-bot-send-images-gifs

# Button timeout (similar to Interaction response time problem):
# https://stackoverflow.com/questions/72312099/discord-py-button-responses-interaction-failed-after-a-certain-time

import discord
from discord.ext import commands
import asyncio
import logging

import io
import os
from dotenv import load_dotenv

import PIL.Image as Image
import numpy as np
import pixelmod


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)


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

def testimage():
    # TODO: make fun rainbow gradient bc why not
    I = np.full((100,100,3), 128).astype(np.uint8)
    I[0:25,0:25,:] = 0
    I[75:100,75:100,:] = 255
    img = Image.fromarray(I)
    img.save("testimage.jpg", quality=95, subsampling=0)
    return "testimage.jpg"

@bot.command()
async def createimage(ctx):
    filepath = testimage()
    await ctx.send(file=discord.File(filepath))
    # TODO: decide on top or bottom method for sending files (which has more memory usage maybe? context manager might auto close or??...)
    # with open(filepath, 'rb') as f:
    #     img = discord.File(f)
    #     await ctx.send(file=img)
    
# https://stackoverflow.com/questions/73361556/error-discord-errors-notfound-404-not-found-error-code-10062-unknown-inter
# @bot.tree.command(description="Randomizes subsets of pixels")
# async def randomslash(interaction:discord.Interaction):
#     await interaction.response.defer()
    
#     channel = interaction.channel
#     img_bytes = None
#     async for msg in channel.history(limit=10):
#         if(len(msg.attachments) == 0):
#             continue
#         if(msg.attachments[0].content_type.startswith("image/") == False):
#             continue
#         img_bytes = await msg.attachments[0].read()
#         break

#     await asyncio.sleep(10)
#     img_bytes_io = io.BytesIO(img_bytes)
#     img = Image.open(img_bytes_io)
#     img = np.copy(np.asarray(img))
#     pixelmod.pixelmod(img, (10,10))
#     img = Image.fromarray(img)
#     img_filepath = "testmodimg.jpg"
#     img.save(img_filepath, quality=95, subsampling=0)
    
#     # await interaction.response.send_message(file=discord.File(img_filepath))
#     await interaction.followup.send(content="slash command", file=discord.File(img_filepath))
#     # NOTE: so likeeeee I don't like having to set a sleep, maybe normal command is the move instead of slash command with interaction

@bot.command()
async def random(ctx:commands.Context):
    # TODO: how to have a "bot is typing" status?
    # TODO: in the image reply, also have image stats like NotSoBot shows
    channel = ctx.channel
    img_bytes = None
    async for msg in channel.history(limit=10):
        if(len(msg.attachments) == 0):
            continue
        if(msg.attachments[0].content_type.startswith("image/") == False):
            continue
        img_bytes = await msg.attachments[0].read()
        break
    
    async with channel.typing():
        img_bytes_io = io.BytesIO(img_bytes)
        img = Image.open(img_bytes_io)
        img = np.copy(np.asarray(img))
        pixelmod.pixelmod(img, (10,10))
        img = Image.fromarray(img)
        img_filepath = "testmodimg.jpg"
        img.save(img_filepath, quality=95, subsampling=0)
    
    await ctx.message.reply(content="dot command", file=discord.File(img_filepath))
    os.remove(img_filepath)




##################################

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot.run(TOKEN)

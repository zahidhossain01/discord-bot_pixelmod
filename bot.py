import discord

import PIL.Image as Image
import numpy as np
import pixelmod

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    
    if msg.content.startswith('$poop'):
        await msg.channel.send('pee!')

TOKEN = 'MTE2MDMwMjg5MjcyOTc3NDE5MA.Gh5Kre.P1OwCPqxx1deUh4Iyj9sMBOotEZX1gPNEAfgwU'
client.run(TOKEN)
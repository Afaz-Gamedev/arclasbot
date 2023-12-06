import os
import discord
from discord import app_commands
import lifeSupport
import httpManage

intents = discord.Intents.default()
client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(client.user)
    await tree.sync(guild=discord.Object(id=1112966445253533726))
    print("Ready!")

@client.event
async def on_message(message) :
  if message.author != client.user:
    print(message)

lifeSupport.keep_alive()
httpManage.test("yo")
my_secret = os.environ['ARCLAS_BOT_SECRET']
client.run(my_secret)
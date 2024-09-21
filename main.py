import discord
from discord.ext import commands

intent = discord.Intents.default()
intent.message_content = True
client = commands.Bot(command_prefix= '!', intents=intent)


@client.event
async def on_ready(): #this function will execute when it is 'ready'
    print("Bot is ready!")
    print("-------------")
    print()

@client.command()
async def hello(ctx):
    await ctx.send("Hi, I am Gizmo")



#the unique bot token is stored in a local txt
try:
    with open('token.txt') as file:
        token = file.read()
except FileNotFoundError:
    FileNotFoundError
client.run(token)

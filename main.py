import discord
from discord.ext import commands
import asyncio

#sensitive info such as (token, channel ID)
#this file is in .gitignore
try:
    with open('token.txt') as file:
        token = file.readline()
        channel_id = int(file.readline())
except FileNotFoundError:
    FileNotFoundError


intent = discord.Intents.default()
intent.message_content = True
intent.members = True
client = commands.Bot(command_prefix= '.', intents=intent)


@client.event
async def on_ready():
    print("We are online and ready!")
    print("-------------")
    print()

@client.event
async def on_member_join(member):
    channel = client.get_channel(channel_id)
    await channel.send("Welcome :wave:, I hope you enjoy your stay :blush:")


@client.command()
async def hello(ctx):
    await ctx.send("Hi, I am Gizmo :smile:")

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("My apologies, I detected that you're not in a voice channel :sweat_smile: \n\
You must be in a voice channel to run this command")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.send("As you wish, goodbye :slight_smile:")
        await asyncio.sleep(1)
        await ctx.guild.voice_client.disconnect()
        
    else:
        await ctx.send("I am currently not in a voice channel")


client.run(token)

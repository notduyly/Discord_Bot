import discord
from discord.ext import commands
import asyncio
from config import *


intent = discord.Intents.default()
intent.message_content = True
intent.members = True
bot = commands.Bot(command_prefix = '.', intents = intent)


@bot.event
async def on_ready():
    print("We are online and ready!")
    print("-------------")
    print()

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(general_txt_channel)
    await channel.send("Welcome :wave:, I hope you enjoy your stay :blush:")

@bot.event
async def on_message(message):
        
    if wake_word in message.content.lower() and message.author != bot.user:
        await message.channel.send("Sorry for the inconvenience :sweat_smile: \n\
:construction: My AI support function is under construction :construction: ")
    else: 
        await bot.process_commands(message)    
        




@bot.command()
async def hello(ctx):
    await ctx.send("Hi, I am Gizmo :smile:")

@bot.command()
async def join(ctx):
    if (ctx.author.voice):
        v_channel = ctx.message.author.voice.channel
        await v_channel.connect()
    else:
        await ctx.send("My apologies, I detected that you're not in a voice channel :sweat_smile: \n\
You must be in a voice channel to run this command")

@bot.command()
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.send("As you wish, goodbye :slight_smile:")
        await asyncio.sleep(1)
        await ctx.guild.voice_client.disconnect()
        
    else:
        await ctx.send("I am currently not in a voice channel")





bot.run(bot_token)

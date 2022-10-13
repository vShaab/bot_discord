from datetime import datetime
from http import server
from http.client import ImproperConnectionState
from locale import strxfrm
from platform import platform
from threading import activeCount
import discord
from discord.ext import commands 
from urllib import parse, request
import re

intents = discord.Intents().all()

bot = commands.Bot(command_prefix= '?', description= 'This is a helper bot', intents= intents)

@bot.command()
async def ping(context):
    await context.send('pong')
# Second command
@bot.command()
async def sum(context, num1:int, num2:int):
    await context.send(num1 + num2)

# Third command
@bot.command()
async def info(context):
    embed = discord.Embed(title= f'{context.guild.name}', 
    description= 'Hola! Soy un nuevo bot creado para ayudarte en este canal',
    color= discord.Color.blue())

    await context.send(embed= embed)

@bot.command()
async def youtube(context, *, search):
    query = parse.urlencode({'search_query': search})
    html_content = request.urlopen('https://www.youtube.com/results?' + query)
    results= re.findall('href=\'\\/watch\\?v=(.{11})', html_content.read().decode())
    # await context.send('https://www.youtube.com/watch?v=' + results[0])
    print(results)

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity= discord.Streaming(platform= 'Twitch', name= 'Showqueando', 
    url= 'https://www.twitch.tv/unfitted_us'))
    print('My Bot is Ready')


bot.run('MTAyOTk3Njc2MzM4OTk3MjU5MQ.G_cnQt.eYx_zO9ampsN45s8ILpA18hxWlifvVS8gYQ93s')

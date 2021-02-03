## Written in discord.py V1.5
## Author: Robert Salisbury(EtaPepper)
## Contact Info: Etapepper#3525 (Discord). edsalisbury7@gmail.com (Email)

## Date of last Edit: 1/21/2021


##IMPORTANT 
## IF THE BOT IS TO BE SHARED PLEASE REMOVE THE TOKEN (bot.run) AT THE BOTTOM OF THE SCRIPT.
##IMPORTANT

import discord
import logging
import pyxivapi

from pyxivapi.models import Filter, Sort
from discord import reaction
import config
from config import botRunKey, xivApiKey
from datetime import datetime  
from datetime import timedelta 
from discord.ext import commands
from random import randint

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)
logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')
discord.Permissions.all() #makes sure that bot can use all permissions

# Discord = require('discord.py')
# client = new Discord.Client()
# config = require("./config.json")

@bot.event
async def on_ready():
    print('Connected!')
    print('Username: ' + bot.user.name)
    print('ID: ' + str(bot.user.id))
    print(discord.__version__)
    print(pyxivapi.__version__)
    print('-------------')


@bot.command()
async def ME(ctx):
    botSend = ctx.message.channel
    

    print(ctx.message.content)

    if ctx.channel == bot.get_channel(562693696038895626):
        xiv = pyxivapi.XIVAPIClient(api_key= config.xivApiKey)

        msg = ctx.message.content.split()

        print(msg)

        fName= msg[1]
        lName= msg[2]

        character = await xiv.character_search(
        world = "Sargatanas",
        forename= fName,
        surname= lName
    )
        await xiv.session.close()
    
        await botSend.send(character)
        
    

########
# Main #
########

if __name__ == "__main__":
    bot.run(config.botRunKey)
    ##xiv = pyxivapi.XIVAPIClient(api_key= config.xivApiKey)
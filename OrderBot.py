## Written in discord.py V1.3
## Author: Robert Salisbury(Senju7)
## Contact Info: Senju7#3525 (Discord). edsalisbury7@gmail.com (Email)
##/home/ubuntu/OrderBotn

## Date of last Edit: 1/21/2021


##IMPORTANT 
## IF THE BOT IS TO BE SHARED PLEASE REMOVE THE TOKEN (bot.run) AT THE BOTTOM OF THE SCRIPT.
##IMPORTANT

import discord
import logging

from discord import reaction
import config
from config import botRunKey
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
    print('-------------')
    

##COMMANDS

@bot.command()
#@commands.cooldown(1, 60, commands.BucketType.user)
async def feed(ctx):
    botSend = ctx.message.channel
    if ctx.channel == bot.get_channel(563375034136133632):
        pass
        phrase = ['test']
        path = 'DiscordBot/feedPhrase.txt'
        f = open(path, "r")
        for line in f:
            phrase.append(line)
        f.close()

        phrase.pop(0)
        x = len(phrase)
        rng = randint(0, x-1)
        fmt = phrase[rng]
                    
        await botSend.send(fmt.format())
    else:
        fmt = 'Please only use this command in #fish-tank'
        await ctx.message.channel.send(fmt.format())

###############
#CLEARING MSG##
###############
@bot.command()
async def clear(ctx):
    user = ctx.message.author
    Guardians = discord.utils.get(ctx.guild.roles, id = 421059593238740993)
    sysAdmin = discord.utils.get(ctx.guild.roles, id = 421313404712648704)
    Leader = discord.utils.get(ctx.guild.roles, id = 420967934035230722)
    botSend = ctx.message.channel
    
    if Guardians in user.roles or sysAdmin in user.roles or Leader in user.roles:

        fmt = 'Clearing Old Messages....'
        await botSend.send(fmt)

        await ctx.channel.purge(limit = None, check = lambda m: not m.pinned)

        fmt = 'Messages Cleared, you can thank {0.mention}.'
        await botSend.send(fmt.format(user))            

    else:
        fmt = '{0.mention}, This is only for Guardians or higher.'
        await botSend.send(fmt.format(user)) 

##EVENTS

@bot.event
async def on_raw_reaction_add(payload):
    guild = bot.get_guild(payload.guild_id)
    user = guild.get_member(payload.user_id)

    #Guild ID
    OrderServerID = 420888977206149131

    #chennal and msg ID's 
    OrderServerID = 420888977206149131
    RulesInfoID = 565679221599502346  #new memebr 
    MemberJoingMsgID = 628745578985160705 #new member

    RoleVenderID = 559167143032258575  #Role Vender
    RoleReactMsgID = 694652842115334164 #The mesg that people will react to for getting nonmandotory roles 

    #Roles gets
    MemberRole = discord.utils.get(guild.roles, name = 'Brave')
    GuestRole = discord.utils.get(guild.roles, name = 'Guest')
    Tank  = discord.utils.get(guild.roles, name = 'Tank')
    Healer = discord.utils.get(guild.roles, name = 'Healer')
    DPS  = discord.utils.get(guild.roles, name = 'DPS')
    Deep_dungeon  = discord.utils.get(guild.roles, name = 'Deep Dungeon')
    Savage  = discord.utils.get(guild.roles, name = 'Savage')
    Extreme  = discord.utils.get(guild.roles, name = 'Extreme')
    Maps  = discord.utils.get(guild.roles, name = 'Maps')
    Roulettes  = discord.utils.get(guild.roles, name = 'Roulettes')
    PC  = discord.utils.get(guild.roles, name = 'PC')
    PS4  = discord.utils.get(guild.roles, name = 'PS4')
    Politics = discord.utils.get(guild.roles, name = 'Politics')
    Rants = discord.utils.get(guild.roles, name = 'Rants')
    exerciseandhealth = discord.utils.get(guild.roles, name = 'Exercise and Health')
    Lotto = discord.utils.get(guild.roles, name = 'Lotto')
    StorySpoiler = discord.utils.get(guild.roles, name = 'Story Spoilers')
    NSFW = discord.utils.get(guild.roles, name = 'NSFW')
    
    #emoji IDS
    EmojiMemberRole = 628731475013009418
    EmojiguestRole = 470677468039086080
    EmojiTank  = 563422622029971487
    EmojiHealer = 563856108557434894
    EmojiDPS  = 563856204372377601
    EmojiDeep_dungeon  = 694640934385614889
    EmojiSavage  = 694643028350206062
    EmojiExtreme  = 694641622549397516
    EmojiMaps  = 694643909917409402
    EmojiRoulettes  = 694644899223699536
    EmojiPC  = 694644200179761163
    EmojiPS4  = 694644184266703018
    EmojiPolitics = 694648263852294161
    EmojiRants = 694679581864493136
    Emojiexerciseandhealth = 694675455625920553
    EmojiLotto = 694341869630521456
    EmojiStorySpoiler = 694341853461610496
    EmojiNSFW = 694656926662918145

    if payload.guild_id != OrderServerID: #checks to see if this is the right sever
        return

    elif payload.channel_id == RulesInfoID and payload.message_id == MemberJoingMsgID: #makes sure that this emjoi is only being checked for this chennal and proper msg
        if payload.emoji.id == EmojiguestRole: #checing guest rules 
            await user.add_roles(GuestRole)
            if user.nick == 'Change Nickname':
                await user.edit(nick = '')
                return

        elif payload.emoji.id == EmojiMemberRole: #checking member(brave) rules
            if user.nick == 'Change Nickname':
                await user.send('Please change your nickname to your in-game name on Final Fantasy XIV.')
                #await MemberJoingMsgID.remove_reaction(EmojiMemberRole, user) #TODO fix remove_reaction after failed use

            elif payload.emoji.id == EmojiMemberRole:
                    await user.add_roles(MemberRole)
            else:
                return
    #This follofing if statment if for info roles that are just cosmetic
    elif payload.channel_id == RoleVenderID and payload.message_id == RoleReactMsgID:
        if payload.emoji.id == EmojiTank:
            await user.add_roles(Tank)
        elif payload.emoji.id == EmojiHealer:
            await user.add_roles(Healer)
        elif payload.emoji.id == EmojiDPS:
            await user.add_roles(DPS)
        elif payload.emoji.id == EmojiDeep_dungeon:
            await user.add_roles(Deep_dungeon)
        elif payload.emoji.id == EmojiSavage:
            await user.add_roles(Savage)
        elif payload.emoji.id == EmojiExtreme:
            await user.add_roles(Extreme)
        elif payload.emoji.id == EmojiMaps:
            await user.add_roles(Maps)
        elif payload.emoji.id == EmojiRoulettes:
            await user.add_roles(Roulettes)
        elif payload.emoji.id == EmojiPC:
            await user.add_roles(PC)
        elif payload.emoji.id == EmojiPS4:
         await user.add_roles(PS4)
        elif payload.emoji.id == EmojiPolitics:
            await user.add_roles(Politics)
        elif payload.emoji.id == EmojiRants:
            await user.add_roles(Rants)
        elif payload.emoji.id == Emojiexerciseandhealth:
            await user.add_roles(exerciseandhealth)
        elif payload.emoji.id == EmojiLotto:
            await user.add_roles(Lotto)
        elif payload.emoji.id == EmojiStorySpoiler:
            await user.add_roles(StorySpoiler)
        elif payload.emoji.id == EmojiNSFW:
            await user.add_roles(NSFW)
        else:
            return
    else: 
        return

    
    

@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    user = guild.get_member(payload.user_id)
    
    #Guild ID
    OrderServerID = 420888977206149131

    #chennal and msg ID's 
    OrderServerID = 420888977206149131
    RulesInfoID = 565679221599502346  #new memebr 
    MemberJoingMsgID = 628745578985160705 #new member

    RoleVenderID = 559167143032258575  #Role Vender
    RoleReactMsgID = 694652842115334164 #The mesg that people will react to for getting nonmandotory roles 

    #Roles gets
    MemberRole = discord.utils.get(guild.roles, name = 'Brave')
    GuestRole = discord.utils.get(guild.roles, name = 'Guest')
    Tank  = discord.utils.get(guild.roles, name = 'Tank')
    Healer = discord.utils.get(guild.roles, name = 'Healer')
    DPS  = discord.utils.get(guild.roles, name = 'DPS')
    Deep_dungeon  = discord.utils.get(guild.roles, name = 'Deep Dungeon')
    Savage  = discord.utils.get(guild.roles, name = 'Savage')
    Extreme  = discord.utils.get(guild.roles, name = 'Extreme')
    Maps  = discord.utils.get(guild.roles, name = 'Maps')
    Roulettes  = discord.utils.get(guild.roles, name = 'Roulettes')
    PC  = discord.utils.get(guild.roles, name = 'PC')
    PS4  = discord.utils.get(guild.roles, name = 'PS4')
    Politics = discord.utils.get(guild.roles, name = 'Politics')
    Rants = discord.utils.get(guild.roles, name = 'Rants')
    exerciseandhealth = discord.utils.get(guild.roles, name = 'Exercise and Health')
    Lotto = discord.utils.get(guild.roles, name = 'Lotto')
    StorySpoiler = discord.utils.get(guild.roles, name = 'Story Spoilers')
    NSFW = discord.utils.get(guild.roles, name = 'NSFW')
    
    #emoji IDS
    EmojiMemberRole = 628731475013009418
    EmojiguestRole = 470677468039086080
    EmojiTank  = 563422622029971487
    EmojiHealer = 563856108557434894
    EmojiDPS  = 563856204372377601
    EmojiDeep_dungeon  = 694640934385614889
    EmojiSavage  = 694643028350206062
    EmojiExtreme  = 694641622549397516
    EmojiMaps  = 694643909917409402
    EmojiRoulettes  = 694644899223699536
    EmojiPC  = 694644200179761163
    EmojiPS4  = 694644184266703018
    EmojiPolitics = 694648263852294161
    EmojiRants = 694679581864493136
    Emojiexerciseandhealth = 694675455625920553
    EmojiLotto = 694341869630521456
    EmojiStorySpoiler = 694341853461610496
    EmojiNSFW = 694656926662918145

    if payload.guild_id != OrderServerID:
        return

    elif payload.channel_id == RulesInfoID or payload.message_id == MemberJoingMsgID:
        if payload.emoji.id == EmojiguestRole:
            await user.remove_roles(GuestRole)
            await user.edit(nick = 'Change Nickname')

        elif payload.emoji.id == EmojiMemberRole:
            await user.remove_roles(MemberRole)
            await user.edit(nick = 'Change Nickname')
        else:
            return
    elif payload.channel_id == RoleVenderID or payload.message_id == RoleReactMsgID:
        if payload.emoji.id == EmojiTank:
            await user.remove_roles(Tank)
        elif payload.emoji.id == EmojiHealer:
            await user.remove_roles(Healer)
        elif payload.emoji.id == EmojiDPS:
            await user.remove_roles(DPS)
        elif payload.emoji.id == EmojiDeep_dungeon:
            await user.remove_roles(Deep_dungeon)
        elif payload.emoji.id == EmojiSavage:
            await user.remove_roles(Savage)
        elif payload.emoji.id == EmojiExtreme:
            await user.remove_roles(Extreme)
        elif payload.emoji.id == EmojiMaps:
            await user.remove_roles(Maps)
        elif payload.emoji.id == EmojiRoulettes:
            await user.remove_roles(Roulettes)
        elif payload.emoji.id == EmojiPC:
            await user.remove_roles(PC)
        elif payload.emoji.id == EmojiPS4:
         await user.remove_roles(PS4)
        elif payload.emoji.id == EmojiPolitics:
            await user.remove_roles(Politics)
        elif payload.emoji.id == EmojiRants:
            await user.remove_roles(Rants)
        elif payload.emoji.id == Emojiexerciseandhealth:
            await user.remove_roles(exerciseandhealth)
        elif payload.emoji.id == EmojiLotto:
            await user.remove_roles(Lotto)
        elif payload.emoji.id == EmojiStorySpoiler:
            await user.remove_roles(StorySpoiler)
        elif payload.emoji.id == EmojiNSFW:
            await user.remove_roles(NSFW)
        else:
            return
    else: 
        return

@bot.event
async def on_member_join(member):
    #guild = member.guild
    
    await member.edit(nick = 'Change Nickname')


##ERROR HANDLERS

@feed.error
async def feed_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        fmt = 'STAHP! I AM EATING ALREADY, FOOLISH MORTAL! ......Feed me again in {:.0f}s'
        await ctx.message.channel.send(fmt.format(error.retry_after))


##CHECKS 


##FUNCTIONS

def venOnly():
    fmt = 'Please only use this command in #vendor'

    return fmt


########
# Main #
########

if __name__ == "__main__":
    bot.run(config.botRunKey)
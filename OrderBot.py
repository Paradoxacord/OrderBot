## Written in discord.py V1.3
## Author: Robert Salisbury(Senju7)
## Contact Info: Senju7#3525 (Discord). edsalisbury7@gmail.com (Email)
##/home/ubuntu/OrderBotn

## Date of last Edit: 10/1/2019


##IMPORTANT 
## IF THE BOT IS TO BE SHARED PLEASE REMOVE THE TOKEN (bot.run) AT THE BOTTOM OF THE SCRIPT.
##IMPORTANT

import discord
import logging
import config
from config import botRunKey
from datetime import datetime  
from datetime import timedelta 
from discord.ext import commands
from random import randint

logger = logging.getLogger('discord')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

# Discord = require('discord.py')
# client = new Discord.Client()
# config = require("./config.json")

@bot.event
async def on_ready():
    print('Connected!')
    print('Username: ' + bot.user.name)
    print('ID: ' + str(bot.user.id))
    print('-------------')
    

##COMMANDS

@bot.command()
async def potd(ctx):
    user = ctx.message.author
    cmdRole = discord.utils.get(ctx.guild.roles, id = 553701469333880853)
    botSend = bot.get_channel(559167143032258575)
    userSent = ctx.channel
    if userSent == botSend:
        if cmdRole in user.roles:
            await user.remove_roles(cmdRole)
            fmt = '{0.mention}, The potd role has been returned.'
            await botSend.send(fmt.format(user))

        else:
            await user.add_roles(cmdRole)
            fmt = '{0.mention}, You now have rented the potd role.'
            await botSend.send(fmt.format(user))
    else:
        fmt = venOnly()
        await ctx.message.channel.send(fmt.format()) 

@bot.command()
async def hoh(ctx):
    user = ctx.message.author
    cmdRole = discord.utils.get(ctx.guild.roles, id = 553701540414881815)
    botSend = bot.get_channel(559167143032258575)
    userSent = ctx.channel

    if userSent == botSend:
        if cmdRole in user.roles:
            await user.remove_roles(cmdRole)
            fmt = '{0.mention}, The hoh role has been returned.'
            await botSend.send(fmt.format(user))

        else:
            await user.add_roles(cmdRole)
            fmt = '{0.mention}, You now have rented the hoh role.'
            await botSend.send(fmt.format(user))
    else:
        fmt = venOnly()
        await ctx.message.channel.send(fmt.format()) 

@bot.command()
async def endgame(ctx):
    user = ctx.message.author
    cmdRole = discord.utils.get(ctx.guild.roles, id = 558110812405891092)
    botSend = bot.get_channel(559167143032258575)
    userSent = ctx.channel

    if userSent == botSend:
        if cmdRole in user.roles:
            await user.remove_roles(cmdRole)
            fmt = '{0.mention}, The End Game role has been returned.'
            await botSend.send(fmt.format(user))

        else:
            await user.add_roles(cmdRole)
            fmt = '{0.mention}, You now have rented the End Game role.'
            await botSend.send(fmt.format(user))
    else:
        fmt = venOnly()
        await ctx.message.channel.send(fmt.format()) 

@bot.command()
async def primal(ctx):
    user = ctx.message.author
    cmdRole = discord.utils.get(ctx.guild.roles, id = 558115501025263626)
    botSend = bot.get_channel(559167143032258575)
    userSent = ctx.channel

    if userSent == botSend:
        if cmdRole in user.roles:
            await user.remove_roles(cmdRole)
            fmt = '{0.mention}, The Primal role has been returned.'
            await botSend.send(fmt.format(user))

        else:
            await user.add_roles(cmdRole)
            fmt = '{0.mention}, You now have rented the Primal role.'
            await botSend.send(fmt.format(user))
    else:
            fmt = venOnly()
            await ctx.message.channel.send(fmt.format())

@bot.command()
async def savage(ctx):
    user = ctx.message.author
    cmdRole = discord.utils.get(ctx.guild.roles, id = 558115504058007552)
    botSend = bot.get_channel(559167143032258575)
    userSent = ctx.channel

    if userSent == botSend:
        if cmdRole in user.roles:
            await user.remove_roles(cmdRole)
            fmt = '{0.mention}, The Savage role has been returned.'
            await botSend.send(fmt.format(user))

        else:
            await user.add_roles(cmdRole)
            fmt = '{0.mention}, You now have rented the Savage role.'
            await botSend.send(fmt.format(user))
    else:
        fmt = venOnly()
        await ctx.message.channel.send(fmt.format())

@bot.command()
async def maps(ctx):
    user = ctx.message.author
    cmdRole = discord.utils.get(ctx.guild.roles, id = 561603061622112257)
    botSend = bot.get_channel(559167143032258575)
    userSent = ctx.channel

    if userSent == botSend:
        if cmdRole in user.roles:
            await user.remove_roles(cmdRole)
            fmt = '{0.mention}, The Maps role has been returned.'
            await botSend.send(fmt.format(user))

        else:
            await user.add_roles(cmdRole)
            fmt = '{0.mention}, You now have rented the Maps role.'
            await botSend.send(fmt.format(user)) 
    else:
        fmt = venOnly()
        await ctx.message.channel.send(fmt.format())

@bot.command()
async def ps4(ctx):
    user = ctx.message.author
    cmdRole = discord.utils.get(ctx.guild.roles, id = 570315799957340160)
    botSend = bot.get_channel(559167143032258575)
    userSent = ctx.channel

    if userSent == botSend:
        if cmdRole in user.roles:
            await user.remove_roles(cmdRole)
            fmt = '{0.mention}, The PS4 role has been returned.'
            await botSend.send(fmt.format(user))

        else:
            await user.add_roles(cmdRole)
            fmt = '{0.mention}, You now have rented the PS4 role.'
            await botSend.send(fmt.format(user)) 
    else:
        fmt = venOnly()
        await ctx.message.channel.send(fmt.format())

@bot.command()
async def pc(ctx):
    user = ctx.message.author
    cmdRole = discord.utils.get(ctx.guild.roles, id = 570315746857451521)
    botSend = bot.get_channel(559167143032258575)
    userSent = ctx.channel

    if userSent == botSend:
        if cmdRole in user.roles:
            await user.remove_roles(cmdRole)
            fmt = '{0.mention}, The PC role has been returned.'
            await botSend.send(fmt.format(user))

        else:
            await user.add_roles(cmdRole)
            fmt = '{0.mention}, You now have rented the PC role.'
            await botSend.send(fmt.format(user)) 
    else:
        fmt = venOnly()
        await ctx.message.channel.send(fmt.format())

@bot.command()
async def tank(ctx):
    user = ctx.message.author
    cmdRole = discord.utils.get(ctx.guild.roles, id = 570655320678858756)
    botSend = bot.get_channel(559167143032258575)
    userSent = ctx.channel

    if userSent == botSend:
        if cmdRole in user.roles:
            await user.remove_roles(cmdRole)
            fmt = '{0.mention}, The Tank role has been returned.'
            await botSend.send(fmt.format(user))

        else:
            await user.add_roles(cmdRole)
            fmt = '{0.mention}, You now have rented the Tank role.'
            await botSend.send(fmt.format(user)) 
    else:
        fmt = venOnly()
        await ctx.message.channel.send(fmt.format())

@bot.command()
async def healer(ctx):
    user = ctx.message.author
    cmdRole = discord.utils.get(ctx.guild.roles, id = 570655323879243846)
    botSend = bot.get_channel(559167143032258575)
    userSent = ctx.channel

    if userSent == botSend:
        if cmdRole in user.roles:
            await user.remove_roles(cmdRole)
            fmt = '{0.mention}, The Healer role has been returned.'
            await botSend.send(fmt.format(user))

        else:
            await user.add_roles(cmdRole)
            fmt = '{0.mention}, You now have rented the Healer role.'
            await botSend.send(fmt.format(user)) 
    else:
        fmt = venOnly()
        await ctx.message.channel.send(fmt.format())

@bot.command()
async def DPS(ctx):
    user = ctx.message.author
    cmdRole = discord.utils.get(ctx.guild.roles, id = 570655325963681805)
    botSend = bot.get_channel(559167143032258575)
    userSent = ctx.channel

    if userSent == botSend:
        if cmdRole in user.roles:
            await user.remove_roles(cmdRole)
            fmt = '{0.mention}, The DPS role has been returned.'
            await botSend.send(fmt.format(user))

        else:
            await user.add_roles(cmdRole)
            fmt = '{0.mention}, You now have rented the DPS role.'
            await botSend.send(fmt.format(user)) 
    else:
        fmt = venOnly()
        await ctx.message.channel.send(fmt.format())

@bot.command()
async def rouls(ctx):
    user = ctx.message.author
    cmdRole = discord.utils.get(ctx.guild.roles, id = 568895719717601295)
    botSend = bot.get_channel(559167143032258575)
    userSent = ctx.channel

    if userSent == botSend:
        if cmdRole in user.roles:
            await user.remove_roles(cmdRole)
            fmt = '{0.mention}, The Roulettes role has been returned.'
            await botSend.send(fmt.format(user))

        else:
            await user.add_roles(cmdRole)
            fmt = '{0.mention}, You now have rented the Roulettes role.'
            await botSend.send(fmt.format(user)) 
    else:
        fmt = venOnly()
        await ctx.message.channel.send(fmt.format())

@bot.command()
async def politics(ctx):
    user = ctx.message.author
    cmdRole = discord.utils.get(ctx.guild.roles, id = 675929622222995466)
    botSend = bot.get_channel(559167143032258575)
    userSent = ctx.channel

    if userSent == botSend:
        if cmdRole in user.roles:
            await user.remove_roles(cmdRole)
            fmt = '{0.mention}, The Politics role has been returned.'
            await botSend.send(fmt.format(user))

        else:
            await user.add_roles(cmdRole)
            fmt = '{0.mention}, You now have rented the Politics role.'
            await botSend.send(fmt.format(user)) 
    else:
        fmt = venOnly()
        await ctx.message.channel.send(fmt.format())


@bot.command()
#@commands.cooldown(1, 60, commands.BucketType.user)
async def feed(ctx):
    botSend = ctx.message.channel
    if ctx.channel == bot.get_channel(563375034136133632):
        pass
        phrase = ['test']
        path = '/home/ubuntu/OrderBot/feedPhrase.txt'
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
    welcome_channel = bot.get_channel(565679221599502346)
    FC_Chat_channel = bot.get_channel(420888977206149133)
    user = guild.get_member(payload.user_id)
    memberRole = discord.utils.get(guild.roles, id = 421288402558648331)
    guestRole = discord.utils.get(guild.roles, id = 514625561188892673)
    message = await bot.get_channel(565679221599502346).fetch_message(628745578985160705)

    if payload.guild_id != 420888977206149131 or payload.channel_id != 565679221599502346 or payload.message_id != 628745578985160705:
        return
    elif payload.emoji.id == 470677468039086080:
        await user.add_roles(guestRole)
        if user.nick == 'Change Nickname':
            await user.edit(nick = '')
    elif user.nick == 'Change Nickname':
        await user.send('Please change your nickname to your in-game name on Final Fantasy XIV.')
        await message.remove_reaction('<:FClogo:628731475013009418>', user)
    elif payload.emoji.id == 628731475013009418:
        await user.add_roles(memberRole)
    else:
        return

@bot.event
async def on_raw_reaction_remove(payload):
    guild = bot.get_guild(payload.guild_id)
    channel = bot.get_channel(565679221599502346)
    user = guild.get_member(payload.user_id)
    memberRole = discord.utils.get(guild.roles, id = 421288402558648331)
    guestRole = discord.utils.get(guild.roles, id = 514625561188892673)
    message = await bot.get_channel(565679221599502346).fetch_message(628745578985160705)

    if payload.guild_id != 420888977206149131 or payload.channel_id != 565679221599502346 or payload.message_id != 628745578985160705:
        return
    elif payload.emoji.id == 470677468039086080:
        await user.remove_roles(guestRole)
        await user.edit(nick = 'Change Nickname')
    elif payload.emoji.id == 628731475013009418:
        await user.remove_roles(memberRole)
        await user.edit(nick = 'Change Nickname')
    else:
        return


@bot.event
async def on_member_join(member):
    guild = member.guild
    
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
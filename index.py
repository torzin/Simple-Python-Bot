import random
import discord
from discord.ext import commands
import logging

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


adm_role_id = 'ADM'
users_role_id = ''


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

#setup command
@bot.command()
async def setup(ctx):
    if ctx.author == ctx.guild.owner:
        await ctx.send("Funcionou")
    else:
        await ctx.send("You don't have permission.")

# funny commands
@bot.command()
async def beauty(ctx, user):
    porcent = random.randint(0 ,100)
    await ctx.send(f"{user} Is {porcent}% Beautiful")

#get the avatar of a especifc user in discord
@bot.command()
async def avatar(ctx, member : discord.Member = None):
    pfp = member.avatar
    embed = discord.Embed(title=f"{member} Here Is Your Picture!", color=0x03fc1c)
    embed.set_image(url=f"{pfp}")
    await ctx.send(embed=embed)

#dice command
@bot.command()
async def dice(ctx):
    number = random.randint(1, 6)
    if number == 1:
        await ctx.send(f"{ctx.author.mention} you rolled {number}🎲😢")
    elif number == 6:
        await ctx.send(f"Congratulations!! {ctx.author.mention} you rolled {number}🎲😆")
    else:
        await ctx.send(f"{ctx.author.mention} you rolled {number}🎲")

# send the user a dm
@bot.command()
async def dm(ctx, user: discord.User, *, reason = None):
    await user.send(f'{reason}')

# ADM Commands

# Kikc Command
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    log = bot.get_channel(1012819523927294003)
    if reason == None:
        reason = 'no reason provided'
    embed = discord.Embed(title=f"User '{member.name}' has been kicked by '{ctx.message.author.name}'")
    embed.add_field(name="Reason:", value=f"{reason}")
    await ctx.guild.kick(member)
    await log.send(embed=embed)

#Ban Command
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    log = bot.get_channel(1012819523927294003)
    if reason == None:
        reason = 'no reason provided'
    embed = discord.Embed(title=f"User '{member.name}' has been kicked by '{ctx.message.author.name}'")
    embed.add_field(name="Reason:", value=f"{reason}")
    await ctx.guild.ban(member)
    await log.send(embed=embed)

#Clear messages command
@bot.command(pass_context = True)
async def clear(ctx, number):
    limit=int(number)
    await ctx.channel.purge(limit=limit)

@bot.event
async def on_message_delete(message):
    log = bot.get_channel(1012819523927294003)
    embed = discord.Embed(title=f"The user '{message.author.name}' deleted a message")
    embed.add_field(name="Message Content:", value=f"{message.content}")
    await log.send(embed=embed)

bot.run('MTAxMTA0NTQyOTgwODQ4MDI3Ng.GwOCOI.6gqbPYKPCAPJVqwDkah7dq3yr2hiGZzWhbxRQw', log_handler=handler, log_level=logging.DEBUG)
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


adm_role_id = ''
users_role_id = ''


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

#setup command
@bot.command()
async def setup(ctx):
    pass


# funny commands
@bot.command()
async def beauty(ctx, user):
    porcent = random.randint(0 ,100)
    await ctx.send(f"{user} Is {porcent}% Beautiful")

@bot.command()
async def avatar(ctx, member : discord.Member = None):
    pfp = member.avatar
    embed = discord.Embed(title=f"{member} Here Is Your Picture!", color=0x03fc1c)
    embed.set_image(url=f"{pfp}")
    await ctx.send(embed=embed)

@bot.command()
async def dice(ctx):
    number = random.randint(1, 6)
    if number == 1:
        await ctx.send(f"{ctx.author.mention} you rolled {number}🎲😢")
    elif number == 6:
        await ctx.send(f"Congratulations!! {ctx.author.mention} you rolled {number}🎲😆")
    else:
        await ctx.send(f"{ctx.author.mention} you rolled {number}🎲")

@bot.command()
async def dm(ctx, user: discord.User, *, reason = None):
    await user.send(f'{reason}')

# ADM Commands

# Kikc Command
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    if reason == None:
        reason = 'no reason provided'
    await ctx.guild.kick(member)
    await ctx.send(f'User {member.mention} has been kicked for {reason}')

#Ban Command
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    if reason == None:
        reason = 'no reason provided'
    await ctx.guild.kick(member)
    await ctx.send(f'User {member.mention} has been kicked for {reason} by {ctx.message.author.name}')

#Clear messages command
@bot.command(pass_context = True)
async def clear(ctx, number):
    limit=int(number)
    await ctx.channel.purge(limit=limit)

@bot.event
async def on_message_delete(message):
    embed = discord.Embed(title=f"The user {message.author} deleted the message",)
    embed.add_field(name='...', value=f"{message.content}")
    log = bot.get_channel("1012819523927294003")
    await log.send(embed=embed)


bot.run("Your Token Here)

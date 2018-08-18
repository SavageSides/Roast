import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import random

TOKEN = 'NDgwMTk2Njk1OTI2MjQzMzM4.DlkR6A.Giw4KdGOjCatMWlZQuIkIHG0vwc'

client = commands.Bot(command_prefix='?')
startup_extensions = ["Music"]

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Type ?roasthelp to get started!'))
    print('Logged in as')
    print(client.user.name)

@client.command(pass_context=True)
@commands.has_role("staff")
async def kick(ctx, user: discord.Member):
    await client.say('{} has been kicked :wave:'.format(user.name))
    await client.kick(user)

@client.command(pass_context=True)
@commands.has_role("staff")
async def ban(ctx, user: discord.Member):
    await client.say('{} has been banned :wave:'.format(user.name))
    await client.ban(user)

@client.command(pass_context=True)
@commands.has_role("staff")
async def ok(ctx, user: discord.Member):
    OkRole = discord.utils.get(ctx.message.server.roles,name='Member')
    UnRole = discord.utils.get(ctx.message.server.roles,name='Unverified')
    await client.say("{} has been verifed!".format(user.name))
    await client.add_roles(user, OkRole)
    await client.remove_roles(user, UnRole)
    await client.add_roles(user, OkRole)

@client.command(pass_context=True)
@commands.has_role("staff")
async def back(ctx, user: discord.Member):
    UnRole = discord.utils.get(ctx.message.server.roles,name='Unverified')
    OkRole = discord.utils.get(ctx.message.server.roles,name='Member')
    await client.say('{} has been put back in verifacation :sob:'.format(user.name))
    await client.add_roles(user, UnRole)
    await client.remove_roles(user, OkRole)
    await client.add_roles(user, UnRole)
    await client.remove_roles(user, OkRole)

@client.command(pass_context=True)
@commands.has_role("staff")
async def mute(ctx, user: discord.Member):
    MutedRole = discord.utils.get(ctx.message.server.roles,name='Muted')
    await client.say('{} has been muted!'.format(user.name))
    await client.add_roles(user, MutedRole)

@client.command(pass_context=True)
@commands.has_role("staff")
async def unmute(ctx, user: discord.Member):
    MutedRole = discord.utils.get(ctx.message.server.roles,name='Muted')
    await client.say('{} has been unmuted!'.format(user.name))
    await client.remove_roles(user, MutedRole)

@client.command(pass_context=True)
@commands.has_role("staff")
async def purge(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('***Messages deleted*** :white_check_mark:')

#Fun

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_author(name="Serverinfo")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def roasthelp(ctx):
    embed = discord.Embed(title="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="info", value='The command is when you can do ?info @user then you will see its info!', inline=True)
    embed.add_field(name="serverinfo", value='Shows you the server info', inline=True)
    embed.add_field(name="Modhelp", value='Tells you mods what commands you can use', inline=True)
    embed.add_field(name="Avatar", value='Shows a users avatar!', inline=True)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s avatar".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.set_thumbnail(url=user.avatar_url)
    await client.say(embed=embed)

#Voice And Music Commands

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

#Auto Generator Commands

@client.command(pass_context=True)
async def roast(context):
    possible_responses = [
        '**Yo mama so fat**',
        '**Your so ugly you got disowned**',
        '**You suck**',
        '**Is it thanksgiving yet cuz yo mama fat as hell!**',
        '**Were my fried chicken at**',
        '**You suck at MooMoo.io!**',
    ]
    await client.say(random.choice(possible_responses) +  ", " + context.message.author.mention)






client.run(TOKEN)

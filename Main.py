import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print("Security Bot Is Online And Ready To Use. Prefix Is !")
    print("Created By KFour For Security Purposes")

@client.command()
async def help(ctx):
    await ctx.send("``Help Menu Is Still Under Construction``")

    client.run('Token Here')
    
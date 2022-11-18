import discord
from discord.ext import commands

TOKEN = 'MTA0MzIyMjAwMDYzMTU1ODE0NQ.GOjevD.TQO9T8y6m5yXKvhnZpfMmtfY_C27WuuCLedP9I'
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print('bot ready')


@client.event
async def on_message(message):
    # channel = client.get_channel(1043285797597610064)
    # await channel.send('testing')
    print(message.author, message.content, message.channel.id)


#     pass


@client.command()
async def hello(ctx):
    channel = client.get_channel(1043285797597610064)
    await channel.send(f'hello there {ctx.author.mention}')


client.run(TOKEN)
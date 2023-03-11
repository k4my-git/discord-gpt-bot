import discord

TOKEN = 'ABCD0123' # TOKENを貼り付け
CHANNELID = 0123456789 # チャンネルIDを貼り付け

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if not message.author.bot:
        channel = client.get_channel(CHANNELID)
        await channel.send(message.content)
        print(message.content)

client.run(TOKEN)
import discord
import sys

client = discord.Client()
token = open("token.txt", "r").read()


@client.event   # event decorator/wrapper
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')
    testbot_guild = client.get_guild(617058807197073422)

    if "!members" == message.content.lower():
        await message.channel.send(f'```py\n{testbot_guild.member_count}```')

    elif "!logout" in message.content.lower():
        await client.close()
        sys.exit()

    elif"!report" == message.content.lower():
        online = 0
        idle = 0
        dnd = 0
        offline = 0

        for m in testbot_guild.members:
            if str(m.status) == "online":
                online += 1
            if str(m.status) == "offline":
                offline += 1
            if str(m.status) == "dnd":
                dnd += 1
            if str(m.status) == "idle":
                idle += 1

        await message.channel.send(f'```Online: {online}\nIdle: {idle}\nDo Not Disturb: {dnd}\nOffline: {offline}```')

client.run(token)

import discord
from discord.ext import commands

with open('TOKEN.txt', 'r') as f:
    TOKEN = f.readline()
    f.close()

description = '''SMS Bot'''
    
    
bot = commands.bot(command_prefix='s!', description=description)

@bot.event()
async def on_ready(self):
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name = 'test', description = "You are already dead...")
async def test(ctx):
    await ctx.send('You have not failed')

@bot.command(name = 'supervan', description = "It's a bird...")
async def supervan(ctx):
    await message.channel.send("It's a bird. It's a plane. No... It's SuperVan!\nhttps://vimeo.com/83319818')

@bot.event
async def on_message(message):
    if 'kevin' in message.content.lower():
        await message.channel.send('He has arrived! Everyone must bow down.')
                                     
bot.run(TOKEN)

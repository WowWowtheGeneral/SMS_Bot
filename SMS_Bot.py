import discord
from discord.ext import commands

with open('TOKEN.txt', 'r') as f:
    TOKEN = f.readline()
    f.close()

description = '''SMS Bot'''

unholy_word_list = ['Airpods', 'Juul', 'Hats', 'Legs', 'Macbooks', 'Weed', 'Cell Phones', 'Bar Mtizvah', 'Bat Mitzvah', 'Kazoos', 'Flip-Flops', 'Spoons', 'Forks', 'Fuck', 'Shit', 'Ass', 'Asshole', 'Dick', 'Bitch']
    
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

@bot.event
async def on_message(message):
    if (unholy_word_list) in message.content.lower():
        await message.channel.send('Woah there buddy! Those words are infernal! You must change your ways and correct your sins. Go here to correct your errors, or the holy beings will disregard you for eternity.\nhttps://docs.google.com/document/d/10x45DFUNA1U0pE8ZYKLO64w_4y6fNGFH9B6M6tlMU3Q/edit') 
                               
bot.run(TOKEN)

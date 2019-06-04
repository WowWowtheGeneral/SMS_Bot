import discord
import random

from discord.ext import commands

with open('TOKEN.txt', 'r') as f:
    TOKEN = f.readline()

DESCRIPTION = '''SMS Bot'''

with open('data/UNHOLY_WORDS.txt', 'r') as f:
    UNHOLY_WORDS = f.readlines()
    for word in UNHOLY_WORDS:
        if word.endswith('\n'):
            num = UNHOLY_WORDS.index(word)
            word = word[:-1]
            UNHOLY_WORDS[num] = word

with open('data/QUOTES.txt', 'r') as f:
    QUOTES = f.readlines()
    for quote in QUOTES:
        if quote.endswith('\n'):
            num = QUOTES.index(quote)
            quote = quote[:-1]
            QUOTES[num] = quote
    
bot = commands.Bot(command_prefix='s!', description=DESCRIPTION)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name = 'test', description = "You are already dead...")
async def test(ctx):
    await ctx.send('You have not failed')

@bot.command(name = 'supervan', description = "It's a bird...")
async def supervan(ctx):
    await ctx.send("It's a bird. It's a plane. No... It's SuperVan!\nhttps://vimeo.com/83319818")
    
@bot.command(name = 'quote', description = "Ms. Clarke's thought of the day")
async def thought(ctx):
        await ctx.send('Here is a thought of the day!\n')
        await ctx.send(random.choice(QUOTES))

@bot.event
async def on_message(message):                                                                        
    if 'kevin' in message.content.lower():
        await message.channel.send('He has arrived! Everyone must bow down.')
    if any([w in message.content.lower() for w in UNHOLY_WORDS  ]):
        await message.channel.send('Woah there buddy! Those words are infernal! You must change your ways and correct your sins. Go here to correct your errors, or the holy beings will disregard you for eternity.\nhttps://docs.google.com/document/d/10x45DFUNA1U0pE8ZYKLO64w_4y6fNGFH9B6M6tlMU3Q/edit')
    await bot.process_commands(message)
                               
bot.run(TOKEN)

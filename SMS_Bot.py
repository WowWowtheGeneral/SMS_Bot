import discord
import random

from discord.ext import commands

with open('TOKEN.txt', 'r') as f:
    TOKEN = f.readline()

DESCRIPTION = '''SMS Bot'''

UNHOLY_WORDS = ['airpods', 'juul', ' hat', 'leg', 'macbook', 'weed', 'phone', 'mitzvah', 'kazoo', 'sandals', 'spoon', 'amos', ' heck', 'hell', 'fork', 'wtf', 'fuck', 'shit', 'ass', 'dick', 'bitch']

QUOTES = ['When something goes down it sinks\n-Ms. Scarborough', 'It would be sort of like the reverse of blowing your nose.\n-Mr. Warren',
"So your sibling built this whole big tower, then you step in and knock it down. It's really good if you can get it on slo-mo camera, you know, perfectly capture the horror on their face... Ah, It's these things that just make me feel alive.\n-Mr.Warren"
, 'Cha Cha YaYa\n-Mrs. Belcher', 'Stop it. Stop it now.\n-Mrs. Belcher', 'Jiminy cricket!\n-Mrs. Belcher', 'Do you want to get your sister *wet* ... with the *HOES*\n-Ms. Scarborough', "I can't hear you, the sun's in my eyes\n-Ms. Grefe"
, "That's not how best friends treat each other\n-Ms. Scarborough"]
    
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
    
@bot.command(name = 'thought', description = "Ms. Clarke's thought of the day")
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

import discord

with open('TOKEN.txt', 'r') as f:
    TOKEN = f.readline()
    f.close()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.lower() == 's!test':
            await message.channel.send('You have not failed')

        if 'kevin' in message.content.lower():
         await message.channel.send('He has arrived! Everyone must bow down!')
        
        if message.content.lower() == 's!supervan':
            await message.channel.send("It's a bird! It's a plane! No, it's SUPERVAN!")
            await message.channel.send('https://vimeo.com/83319818')

client = MyClient()
client.run(TOKEN)

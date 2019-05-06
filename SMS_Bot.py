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

        if message.content == 's!test':
            await message.channel.send('You have not failed') 

client = MyClient()
client.run(TOKEN)

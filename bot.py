# bot.py
import os
import discord
import openai
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

# Set up the OpenAI API client
openai.api_key = OPENAI_KEY

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# test sending a message and receiving something back from the bot
'''@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('Hello Mr. BotFace'):
        await message.channel.send('Howdy Stranger')'''

@client.event
async def on_message(message):
    # Only respond to messages from other users, not from the bot itself
    if message.author == client.user:
        return

    # Check if the bot is mentioned in the message
    if client.user in message.mentions:

        # Use the OpenAI API to generate a response to the message
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{message.content}",
            max_tokens=2048,
            temperature=0.5,
        )

        # Send the response as a message
        await message.channel.send(response.choices[0].text)

# Start the bot
client.run(TOKEN)

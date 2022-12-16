import discord
import os
import pycld2
from dotenv import load_dotenv
import requests
import json


load_dotenv()

TOKEN = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content:
        if len(message.content) > 4:
            isReliable, textBytesFound, details = pycld2.detect(message.content)
            lang = str(details[0][1])
            if lang != 'ja':
                if lang == 'un':
                    lang = ''
                result = requests.get(f'https://script.google.com/macros/s/AKfycbw4lJ0oQDyEd9SBUAK8nziUWk6-SpFgC09ui1sPa-6Z9KinT3eigEBml8TlOiRvqX-Y/exec?text={message.content}&source={lang}&target=ja')
                rdata = json.loads(result.text)

                if rdata['code'] == 200:
                    reply = f'{rdata["text"]}'
                    await message.channel.send(reply)

client.run(TOKEN)
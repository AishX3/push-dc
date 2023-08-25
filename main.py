import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

responses = [
    "Pesan balasan otomatis 1",
    "Pesan balasan otomatis 2",
    "Pesan balasan otomatis 3",
    "Pesan balasan otomatis 4"
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author != bot.user and message.channel.id == 976132165450473512:
        response = random.choice(responses)
        await message.channel.send(response)

    await bot.process_commands(message)

bot.run('OTMzNTg4MTg2OTc2ODkwOTIy.GhWKgt.5ZI6VIyFLSded0vTw6wArkbDV_kQUv1VhHT_qo')

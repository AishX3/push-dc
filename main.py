import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

responses = [
    "bang bang1",
    "mbja",
    "apasi",
    "Pesan balasan otomatis 4"
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # Cek apakah pesan bukan dari bot sendiri dan dalam saluran yang diinginkan
    if message.author != bot.user and message.channel.id == 976132165450473512:
        response = random.choice(responses)  # Memilih pesan secara acak
        await message.channel.send(response)

    await bot.process_commands(message)  # Penting untuk memproses perintah bot

bot.run(NTg5MTU5OTgwODAwODAyODI2.Gg3gjt.l_QbHZtDvOqsJqQB6F5ya2gq2XNDFDc7EGxqX4)

import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.presences = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

with open("pesan.txt", "r") as f:
    responses = f.readlines()

with open("token.txt", "r") as f:
    bot_token = f.readline().strip()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    # Cek apakah pesan bukan dari bot sendiri dan dalam saluran yang diinginkan
    if message.author != bot.user and message.channel.id == YOUR_CHANNEL_ID:
        response = random.choice(responses).strip()  # Memilih pesan secara acak
        await message.channel.send(response)

    await bot.process_commands(message)  # Penting untuk memproses perintah bot

if __name__ == "__main__":
    # Meminta input ID saluran dari user setelah menjalankan skrip
    YOUR_CHANNEL_ID = int(input("Masukkan ID channel: "))
    
    # Memastikan ID saluran yang dimasukkan valid (berupa angka)
    if not YOUR_CHANNEL_ID:
        print("ID channel tidak valid.")
        exit(1)

    bot.run(bot_token)

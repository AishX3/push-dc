import discord
from discord.ext import commands
import random
import sys  # Import modul sys untuk mengakses argumen dari command line

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
    if len(sys.argv) < 2:
        print("Usage: python main.py <channel_id>")
        sys.exit(1)

    YOUR_CHANNEL_ID = int(sys.argv[1])  # Mengambil channel ID dari argumen command line

    bot.run(bot_token)

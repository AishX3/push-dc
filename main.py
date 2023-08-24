import requests
import random
import time
import os
from colorama import Fore

# Input ID channel dari user
channel_id = input("Masukkan ID channel: ")

waktu2 = int(input("Set Waktu Kirim Pesan: "))  # Menyimpan waktu antara pengiriman pesan

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

with open("pesan.txt", "r") as f:
    words = f.readlines()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
    channel_id = channel_id.strip()

    payload = {
        'content': random.choice(words).strip()
    }

    headers = {
        'Authorization': authorization
    }

    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
    print(Fore.WHITE + "Sent message: ")
    print(Fore.YELLOW + payload['content'])

    time.sleep(waktu2)  # Menunggu waktu antara pengiriman pesan

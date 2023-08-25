import requests
import time
import os
from colorama import Fore

time.sleep(1)

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

# Inisialisasi variabel untuk melacak indeks pesan
indeks_pesan = 0

while True:
    channel_id = channel_id.strip()

    # Memastikan indeks tidak melampaui panjang daftar pesan
    if indeks_pesan >= len(words):
        break

    pesan = words[indeks_pesan].strip()

    payload = {
        'content': pesan
    }

    headers = {
        'Authorization': authorization
    }

    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
    print(Fore.WHITE + "Sent message: ")
    print(Fore.YELLOW + pesan)

    # Menaikkan indeks pesan
    indeks_pesan += 1

    time.sleep(waktu2)  # Menunggu waktu antara pengiriman pesan

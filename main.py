import requests
import random
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

# Inisialisasi variabel untuk menyimpan pesan yang telah dikirim
pesan_terkirim = ""

while True:
    channel_id = channel_id.strip()

    # Pilih pesan secara acak yang belum terkirim sebelumnya
    pesan = random.choice(words).strip()
    while pesan == pesan_terkirim:
        pesan = random.choice(words).strip()

    payload = {
        'content': pesan
    }

    headers = {
        'Authorization': authorization
    }

    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
    print(Fore.WHITE + "Sent message: ")
    print(Fore.YELLOW + pesan)

    # Simpan pesan yang telah dikirim
    pesan_terkirim = pesan

    time.sleep(waktu2)  # Menunggu waktu antara pengiriman pesan

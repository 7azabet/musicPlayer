#!/usr/bin/env python3
# Will Being Coded By: Nader.

from pygame import mixer
from os import system

musicFile = input("Musicð¶?: ")
system("clear")

mixer.init()

vol = 0.5

try:
    mixer.music.load(f"{musicFile}")
except Exception as e:
    print(e)  # Module format not recognized
    exit()

mixer.music.set_volume(vol)
mixer.music.play(-1)

print(
    "\nType 'p' to pause or 'r' to resume.\nType '+' to increase volume or '-' to decrease volume.\nType 'res' to "
    "restart the music.\nType 'e' to exit.\n")

while 1:
    query = input(u"ðµ (ã£â¯ðï¸ï¸ â¯ÍÊ ï¸¡ðï¸)ã£ð > ").lower()
    if query == 'p':
        mixer.music.pause()
        print("[â«] Music has been paused.")
    elif query == 'r':
        mixer.music.unpause()
        print("[â«] Music has been played.")
    elif query == '+':
        vol += 0.2
        mixer.music.set_volume(vol)
        print(f"[â«] Volume has been increased by '0.2'\nThe current value of volume is {mixer.music.get_volume()} .")
    elif query == '-':
        vol -= 0.2
        mixer.music.set_volume(vol)
        print(f"[â«] Volume has been decreased by '0.2'\nThe current value of volume is {mixer.music.get_volume()} .")
    elif query == "res":
        mixer.music.rewind()
        print("[â«] Music has been restarted .")
    elif query == 'e':
        mixer.music.stop()
        print("Goodbye ð¶ð¶")
        break
    else:
        print("[â¬] Enter an invalid argument.")

# Was Coded By: Nader.

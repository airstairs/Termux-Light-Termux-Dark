import os
import time

os.system("clear")
print("installing termux-light[termux-dark]")
time.sleep(1)
os.system("clear")
print("copying tool to the .termux directory")
time.sleep(1)

# copy the tool to the .termux directory
os.system("cp -rfv termuxdarklight ~/.termux/.")

time.sleep(3)
os.system("clear")
print("adding termux-dark and termux-light aliases to ~/.bashrc")

# preload .termux with one of the font.tff files so it can perform the swap based on instructions in scripts
os.system("cp ~/.termux/termuxdarklight/dark/font.ttf ~/.termux/.")
# add the termux-dark and termux-light alias to the bashrc
alias_dark = "alias termux-dark='python ~/.termux/termuxdarklight/dark.py'"
alias_light= "alias termux-light='python ~/.termux/termuxdarklight/light.py'"
os.system(f'echo "{alias_dark}" >> ~/.bashrc')
os.system(f'echo "{alias_light}" >> ~/.bashrc')




time.sleep(3)

os.system("clear")
print("termux-light[termux-dark] done installing\n will  kill termux now so that on fresh load the commands work:\ntermux-light\ntermux-dark")
time.sleep(4)
print("\n\n\n press enter to kill termux [needs restart for dark and light theme to work]")
close = input()

os.system("pkill -u $(whoami)")


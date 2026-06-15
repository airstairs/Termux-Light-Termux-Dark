import os

os.system("cat ~/.termux/termuxdarklight/dark/termux.properties > ~/.termux/termux.properties")
os.system("cat ~/.termux/termuxdarklight/dark/colors.properties > ~/.termux/colors.properties")
os.system("rm ~/.termux/font.ttf && cp ~/.termux/termuxdarklight/dark/font.ttf ~/.termux/.")
os.system("termux-reload-settings")


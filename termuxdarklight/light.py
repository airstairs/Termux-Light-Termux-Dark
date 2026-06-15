import os

os.system("cat ~/.termux/termuxdarklight/light/termux.properties > ~/.termux/termux.properties")
os.system("cat ~/.termux/termuxdarklight/light/colors.properties > ~/.termux/colors.properties")
os.system("rm ~/.termux/font.ttf && cp ~/.termux/termuxdarklight/light/font.ttf ~/.termux/.")
os.system("termux-reload-settings")


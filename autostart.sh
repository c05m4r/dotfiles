#!/bin/bash
redshift -O 3000 &
feh --bg-scale ~/dotfiles/wallpapers/wallpaper4.jpg &
sleep 10
python3 $HOME/GIT/dotfiles/battery_status/battery_status.py &
#diodon &
#conky -c ~/dotfiles/.config/conky/conky.conf &

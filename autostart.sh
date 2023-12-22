#!/bin/bash
redshift -O 3000 &
feh --bg-scale $HOME/dotfiles/wallpapers/wallpaper5.jpg &
sleep 10
python3 $HOME/dotfiles/battery_status/battery_status.py &
#conky -c ~/dotfiles/.config/conky/conky.conf &

#!/bin/bash
redshift -O 3000 &
feh --bg-scale ~/dotfiles/wallpapers/wallpaper4.jpg &
sleep 10
diodon &
conky -c ~/dotfiles/.config/conky/conky.conf &

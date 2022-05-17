#!/bin/bash
dnf update -y && dnf upgrade -y --refresh
dnf install -y htop \
	bat \
	lsd \
        mc \
        neofetch \
        git \
        ncdu \
        neovim \
        powerline \
        fzf \
        kitty \
        feh \
        rofi \
	polybar \
	keepassxc \
	redshift \
        conky \
        firefox \
#flatpak
flatpak install flathub com.brave.Browser
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
#configure
dnf clean all
dnf autoremove -y
#oh-my-bash, nerd-fonts, megasync, google-chrome, vlc, wacom-firmware

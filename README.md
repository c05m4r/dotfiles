## Dotfiles

> Personalizacion realizada en Arch, Fedora y Ubuntu

<!-- ## Fuentes -->
<details>
<summary>Fuentes</summary>
    
> Para evitar conflictos instalar Nerd Fonts, Powerline, Awesome. Nerd Fonts incluye estas últimas.
* [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts/blob/master/readme.md)
* [Powerline](https://github.com/powerline/fonts)
* [Awesome](https://github.com/FortAwesome/Font-Awesome)
#### Otras fuentes
* [Cascadia Code](https://github.com/microsoft/cascadia-code)
* [Devicons](https://github.com/vorillaz/devicons)
* [Octicons](https://github.com/primer/octicons)
* [Powerline Extra](https://github.com/ryanoasis/powerline-extra-symbols)
* [Weather](https://github.com/erikflowers/weather-icons)
* [Font](https://github.com/lukas-w/font-logos)
* [Awesome Extension](https://github.com/AndreLZGava/font-awesome-extension)
</details>
<!-- ## Terminal -->
<details>
<summary>Terminal</summary>
<!-- ### Shell -->
<details>
<summary>Shell</summary>

#### Oh My Bash
Un framework para administrar las configuraciones del interprete BASH facilmente.
* [OhMyBash](https://github.com/ohmybash/oh-my-bash)
#### Oh My Zsh
Un framework para administrar las configuraciones del interprete ZSH facilmente.
* [OhMyZsh](https://github.com/ohmyzsh/ohmyzsh)
#### Oh My Fish
Un framework para administrar las configuraciones del interprete Fish facilmente.
* [OhMyFish](https://github.com/oh-my-fish/oh-my-fish)
</details>
<!-- ### Emuladores -->
<details>
<summary>Emuladores</summary>

#### Alacritty
Un ligero emulador de terminal acelerado por GPU desarrollado en Rust.
* [alacritty](https://github.com/alacritty/alacritty)
#### Kitty
Un ligero emulador de terminal acelerado por GPU desarrollado en Python y C.
* [kitty](https://github.com/kovidgoyal/kitty)
#### Cool Retro Term
A good looking terminal emulator which mimics the old cathode display...
* [cool-retro-term](https://github.com/Swordfish90/cool-retro-term)
<!-- ##### Ayuda -->
<details>
<summary>Ayuda</summary>

> Establecer alacritty como terminal por defecto.
```bash
sudo update-alternatives --install /usr/bin/x-terminal-emulator x-terminal-emulator /usr/bin/alacritty 50
sudo update-alternatives --config x-terminal-emulator
```
</details>
</details>

<!-- ### Screensavers -->
<details>
<summary>Screensavers</summary>

#### xscreensaver
XScreenSaver is the standard screen saver collection shipped on most Linux and Unix systems running the X11 Window System.
* [xscreensaver](https://www.jwz.org/xscreensaver/)
#### cmatrix
Terminal based "The Matrix" like implementation.
* [cmatrix](https://github.com/abishekvashok/cmatrix)
#### pipes.sh
Animated pipes terminal screensaver.
* [pipes.sh](https://github.com/pipeseroni/pipes.sh)
#### pipes.c
Small application to mimic the "pipes" screensaver in a terminal window.
* [pipes.c](https://github.com/pipeseroni/pipes.c)
#### snakes.pl
Pipes-like terminal screensaver implemented in perl.
* [snakes.pl](https://github.com/pipeseroni/snakes.pl)
#### maze.py
Simple curses pipes written in Python.
* [maze.py](https://github.com/pipeseroni/maze.py)
#### pipesX.sh
Animated pipes terminal screensaver at an angle.
* [pipesX.sh](https://github.com/pipeseroni/pipesX.sh)
#### weave.sh
Weaving in terminal
* [weave.sh](https://github.com/pipeseroni/weave.sh)
#### hollywood
* [hollywood](https://github.com/dustinkirkland/hollywood)
#### oneko
The program oneko creates a cute cat chasing around your mouse cursor.
* [oneko](http://www.daidouji.com/oneko/)
</details>
<!-- ### Editores de texto -->
<details>
<summary>Editores de texto</summary>

#### Xi-Editor
Un moderno editor de text con un backend escrito en Rust.
* [xi](https://xi-editor.io/)
#### Nano
Un simple y pequeño editor de codigo inspirado en Pico.
* [nano](https://git.savannah.gnu.org/cgit/nano.git/)
#### Emacs
Un extensible y customizable editor de texto libre.
* [emacs](https://github.com/emacs-mirror/emacs)
#### Vi
Un editor de texto tradicional portado por sistemas Unix modernos.
* [vi](https://sourceforge.net/projects/ex-vi/)
#### Vim
Un editor de texto configurable creado para una escritura rapida y eficiente.
* [vim](https://github.com/vim/vim)
#### Neovim
Un fork de Vim refactorizado en búsqueda de la extensibilidad y simplificar el mantenimiento.
* [Neovim](https://github.com/neovim/neovim)
* [Aprender Vim Jugando](https://vim-adventures.com/)
* [Configura Vim por una interfaz](https://vim-bootstrap.com/)
* [Personaliza la linea de estado de Vim](https://github.com/vim-airline/vim-airline)
* [Añade Plugins a Vim](https://github.com/junegunn/vim-plug)
* [Multicursores en Vim?](https://github.com/terryma/vim-multiple-cursors)
* [Volver a Vim inteligente](https://github.com/neoclide/coc.nvim)
<!-- ##### Ayuda -->
<details>
<summary>Ayuda</summary>

> Para reparar neovim ingresar el siguiente comando y seguir las instrucciones.
```vim
:checkhealth
```
</details>
</details>
<!-- ### Administradores de Archivos -->
<details>
<summary>Administradores de Archivos</summary>

#### Ranger
A VIM-inspired filemanager for the console. See [ueberzug](https://github.com/seebye/ueberzug#installation) plugin.
* [ranger](https://github.com/ranger/ranger)
#### Midnight Commander
GNU Midnight Commander es un shell de usuario con interfaz en modo texto para administrar archivos.
* [mc](https://github.com/MidnightCommander/mc)
#### XFE
X File Explorer es un administrador de archivos similar a MS-Explorer para X.
* [xfe](https://sourceforge.net/projects/xfe/)
</details>
<!-- ### Navegadores -->
<details>
<summary>Navegadores</summary>

#### ELinks
Es un navegador WWW en modo texto, compatible con colores, representación de tablas, descarga en segundo plano, interfaz de configuración basada en menús, navegación con pestañas y código reducido.
* [elinks](https://linux.die.net/man/1/elinks)
#### Links
Links es un navegador de modo gráfico y texto, publicado bajo licencia GPL.
* [links](http://links.twibright.com/)
#### Lynx
Lynx es un navegador de texto para la World Wide Web.
* [lynx](https://lynx.browser.org/)
#### Otros navergadores
* [retawq](http://retawq.sourceforge.net/)
* [edbrowse](http://edbrowse.sourceforge.net/)
* [netrik](http://netrik.sourceforge.net/)
* [w3m](http://w3m.sourceforge.net/)
* [Interesante discusión sobre navergadores](https://www.reddit.com/r/commandline/comments/6ck33i/comparing_textmode_browsers_lynx_vs_links_vs/)
</details>
</details>
<!-- ## Administradores de Ventanas (WM) -->
<details>
<summary>Administradores de Ventanas (WM)</summary>

#### Qtile
Un administrador de ventanas de mosaico con todas las funciones escritas y configuradas en Python.
* [qtile](https://github.com/qtile/qtile)

#### Otros WM
* [awesome](https://awesomewm.org/)
* [i3](https://i3wm.org/)
* [openbox](http://openbox.org/wiki/Main_Page)
* [i3-gaps](https://github.com/Airblader/i3)
* [xmonad](https://xmonad.org/)
* [dwm](https://dwm.suckless.org/)
* [spectrwm](https://github.com/conformal/spectrwm#readme)
<!-- ##### Ayuda -->
<details>
<summary>Ayuda</summary>

> Si instalas desde el código fuente, crear el siguiente enlace simbólico.
```bash
ln -s ~/.local/bin/qtile /usr/bin/qtile 
```
> Para poder seleccionar qtile en lightdm crear este [archivo](https://github.com/qtile/qtile/blob/master/resources/qtile.desktop).
```bash
sudo echo -e "\
[Desktop Entry]\
\nName=Qtile \
\nComment=Qtile Session\
\nExec=qtile start\
\nType=Application\
\nKeywords=wm;tiling"\
>> /usr/share/xsessions/qtile.desktop
```
> Para ejecutar autostart.sh, se deben dar permisos de ejecucion al script.
```bash
sudo chmod +x ~/dotfiles/autostart.sh
```
> Para salvar problemas con xbacklight y teclas de brillo [LEER](https://askubuntu.com/questions/715306/xbacklight-no-outputs-have-backlight-property-no-sys-class-backlight-folder#715310)

> Para salvar: HDMI "No Signal" [LEER](https://9to5linux.com/how-to-connect-your-laptop-to-an-external-monitor-on-linux-fix-for-hdmi-no-signal-issue)
```bash
glxinfo | egrep "OpenGL vendor|OpenGL renderer"
sudo cp -p /usr/share/X11/xorg.conf.d/10-amdgpu.conf /etc/X11/xorg.conf.d/10-amdgpu.conf
```
> o puede salvarse instalando [xcompmgr](https://gitlab.freedesktop.org/xorg/app/xcompmgr/)

> Ver personalizacion de [Antonio Sarosi](https://github.com/antoniosarosi/dotfiles/tree/master/.config/qtile)
</details>
</details>
<!-- ## Gestores de Inicio de Sesión (DM) -->
<details>
<summary>Gestores de Inicio de Sesión (DM)</summary>

#### GNOME Display Manager (GDM)
The GNOME Display Manager (GDM) is a program that manages graphical display servers and handles graphical user logins.
* [gdm](https://wiki.gnome.org/Projects/GDM)
#### Lightwight Display Manager (LXDM)
Lightweight display manager for the LXDE desktop environment.
* [lxdm](https://wiki.lxde.org/)
#### Simple Desktop Display Manager (SDDM)
QML based X11 and Wayland display manager
* [sddm](https://github.com/sddm/sddm)
#### Light Display Manager (LightDM)
* [ldm](https://github.com/canonical/lightdm)
#### ly
Display manager with console UI
* [ly](https://github.com/fairyglade/ly)
> [Otros DM recomendados.](https://wiki.archlinux.org/title/Display_manager)
</details>

<!-- ## Otras Herramientas -->
<details>
<summary>Otras Herramientas</summary>

#### BAT
Un clon de cat pero mucho mas elegante.
* [bat](https://github.com/sharkdp/bat/)
#### LSD
Un clon de ls pero mucho mas elegante.
* [lsd](https://github.com/Peltoche/lsd)
#### EXA
Un moderno reemplazo para 'ls'
* [exa](https://github.com/ogham/exa)
#### HTOP
Un monitor de procesos para terminal con ncurses como interfaz.
* [htop](https://github.com/htop-dev/htop)
#### NCurses Disk Usage
Un analizador de uso de disco con ncurses como interfaz.
* [ncdu](https://dev.yorhel.nl/ncdu)
#### Alsa Mixer
Mixer para Alsa, un driver de tarjetas de sonido, con ncurses como interfaz.
* [alsamixer](https://linux.die.net/man/1/alsamixer)
#### NMCLI
Una herramienta de linea de comandos para controlar NetworkManager y obtener su estado.
* [nmcli](https://linux.die.net/man/1/nmcli)
#### IWD
iNet Wireless Daemon project aims to provide a comprehensive Wi-Fi connectivity solution for Linux based devices.
* [iwd](https://iwd.wiki.kernel.org/)
#### FZF
A command-line fuzzy finder.
* [fzf](https://github.com/junegunn/fzf)
#### Z
Busca directorio según su frecuencia.
* [z](https://github.com/rupa/z)
#### Autojump
Un comando 'cd' que aprende.
* [autojump](https://github.com/wting/autojump)
#### MAN
Una interfaz para los manuales de referencia del sistema.
* [man](https://gitlab.com/cjwatson/man-db/)
#### tldr
Hojas de referencia colaborativas para comandos de consola.
* [tldr](https://github.com/tldr-pages/tldr)
#### ROFI
Un lanzador de aplicaciones minimalista.
* [rofi](https://github.com/davatorium/rofi)
#### FEH
Un visor de imágenes X11 dirigido principalmente a usuarios de consolas.
* [feh](https://feh.finalrewind.org/)
#### Nitrogen
Navegador de fondo y setter para X windows.
* [nitrogen](https://github.com/l3ib/nitrogen/)
#### Azote
Wallpaper and colour manager for Sway, i3 and some other WMs.
* [azote](https://github.com/nwg-piotr/azote)
</details>
<!-- ## Personalización -->
<details>
<summary>Personalización</summary>

#### Bumblebee
Es un generador de línea de estado modular y compatible con temas para el administrador de ventanas i3.
* [bumblebee](https://github.com/tobi-wan-kenobi/bumblebee-status)
#### Conky
Es un monitor de sistema liviano y gratuito para X, que muestra cualquier tipo de información en su escritorio.
* [conky](https://github.com/brndnmtthws/conky)
> Se recomienda leer **README.md** en **~/dotfiles/.config/conky**.
#### Polybar
Una barra de estado rápida y fácil de usar. Polybar tiene como objetivo ayudar a los usuarios a crear barras de estado hermosas y altamente personalizables para su entorno de escritorio, sin la necesidad de tener un cinturón negro en scripts de shell.
* [polybar](https://github.com/polybar/polybar)
#### Picom
Es un compositor para X y un fork de Compton.
* [picom](https://github.com/yshui/picom)
#### Compton
Es un compositor para X. Es un fork de xcompmgr de Dana Jansens y se refactorizó.
* [compton](https://github.com/chjj/compton/)
</details>

> Ver screenshots en src/

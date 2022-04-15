# Personalizacion realizada en Ubuntu
## Fuentes
Para evitar conflictos instalar Nerd Fonts, Powerline, Awesome. Nerd Fonts incluye estas últimas.
* [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts/blob/master/readme.md)
* [Powerline](https://github.com/powerline/fonts)
* [Awesome](https://github.com/FortAwesome/Font-Awesome)
## Terminal
### Shell
#### Oh My Bash
Un framework para administrar las configuraciones del interprete BASH facilmente.
* [OhMyBash](https://github.com/ohmybash/oh-my-bash)
#### Oh My Zsh
Un framework para administrar las configuraciones del interprete ZSH facilmente.
* [OhMyZsh](https://github.com/ohmyzsh/ohmyzsh)
#### Oh My Fish
Un framework para administrar las configuraciones del interprete Fish facilmente.
* [OhMyFish](https://github.com/oh-my-fish/oh-my-fish)
### Emuladores
#### Alacritty
Un ligero emulador de terminal acelerado por GPU desarrollado en Rust.
* [alacritty](https://github.com/alacritty/alacritty)
#### Kitty
Un ligero emulador de terminal acelerado por GPU desarrollado en Python y C.
* [kitty](https://github.com/kovidgoyal/kitty)
##### Ayuda
Establecer alacritty como terminal por defecto.
```bash
sudo update-alternatives --install /usr/bin/x-terminal-emulator x-terminal-emulator /usr/bin/alacritty 50
sudo update-alternatives --config x-terminal-emulator
```
### Editores de texto
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
##### Ayuda
Para reparar neovim ingresar el siguiente comando y seguir las instrucciones.
```vim
:checkhealth
```
### Administradores de Archivos
#### Midnight Commander
GNU Midnight Commander es un shell de usuario con interfaz en modo texto para administrar archivos.
* [mc](https://github.com/MidnightCommander/mc)
#### XFE
X File Explorer es un administrador de archivos similar a MS-Explorer para X.
* [xfe](https://sourceforge.net/projects/xfe/)
### Navegadores
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
##### Ayuda
* [Interesante discusión sobre navergadores](https://www.reddit.com/r/commandline/comments/6ck33i/comparing_textmode_browsers_lynx_vs_links_vs/)
##Administradores de Ventanas (WM)
#### Qtile
Un administrador de ventanas de mosaico con todas las funciones escritas y configuradas en Python.
* [qtile](https://github.com/qtile/qtile)
##### Ayuda
Si instalas desde el código fuente, crear el siguiente enlace simbólico.
```bash
ln -s ~/.local/bin/qtile /usr/bin/qtile 
```
Para poder seleccionar qtile en lightdm crear este [archivo](https://github.com/qtile/qtile/blob/master/resources/qtile.desktop).
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
Para ejecutar autostart.sh, se deben dar permisos de ejecucion al script.
```bash
sudo chmod +x ~/dotfiles/autostart.sh
```
## Otras Herramientas
#### BAT
Un clon de cat pero mucho mas elegante.
* [bat](https://github.com/sharkdp/bat/)
#### LSD
Un clon de ls pero mucho mas elegante.
* [lsd](https://github.com/Peltoche/lsd)
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
#### FZF
A command-line fuzzy finder.
* [fzf](https://github.com/junegunn/fzf)
#### ROFI
Un lanzador de aplicaciones minimalista.
* [rofi](https://github.com/davatorium/rofi)
#### FEH
Un visor de imágenes X11 dirigido principalmente a usuarios de consolas.
* [feh](https://feh.finalrewind.org/)
#### Nitrogen
Navegador de fondo y setter para X windows.
* [nitrogen](https://github.com/l3ib/nitrogen/)
## Personalización
#### Bumblebee
Es un generador de línea de estado modular y compatible con temas para el administrador de ventanas i3.
* [bumblebee](https://github.com/tobi-wan-kenobi/bumblebee-status)
#### Conky
Es un monitor de sistema liviano y gratuito para X, que muestra cualquier tipo de información en su escritorio.
* [conky](https://github.com/brndnmtthws/conky)
#### Polybar
Una barra de estado rápida y fácil de usar. Polybar tiene como objetivo ayudar a los usuarios a crear barras de estado hermosas y altamente personalizables para su entorno de escritorio, sin la necesidad de tener un cinturón negro en scripts de shell.
* [polybar](https://github.com/polybar/polybar)
#### Picom
Es un compositor para X y un fork de Compton.
* [picom](https://github.com/yshui/picom)
#### Compton
Es un compositor para X. Es un fork de xcompmgr de Dana Jansens y se refactorizó.
* [compton](https://github.com/chjj/compton/)

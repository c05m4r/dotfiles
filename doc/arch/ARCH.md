# Arch

## ¿Qué es Arch?
Arch es desarrollado por el canadiense **Judd Vinet** lanzando *Arch 0.1* el **11 de marzo de 2002**. Actualmente el mando del proyecto pertenece a **Aaron Griffin**.

Es creado cubrir imperfectos de Crux:
* falta de metadatos
* falta de seguimiento de dependencias
* complejidad para localizar y descargar paquetes

> Es de propósito general, en sus inicios Judd lo usó para sus servidores, pero actualmente inspira a distribuciones workstation como:
* [Manjaro](https://manjaro.org/)
* [Black Arch](https://www.blackarch.org/)
* [Arco Linux](https://arcolinux.com/)
* [Arch Strike](https://archstrike.org/)
* [Antergos](https://antergos.com/)


### Filosofía
* La comunidad se mueve bajo la filosofía de “Hágalo usted mismo”.
* Centrada en el minimalismo.
* Su comunidad es participativa y con una wiki inmensa.
* Su instalación no es sencilla pero es garante de una experiencia satisfactoria.

### ¿Qué lo diferencia?
<details>
<summary>Rolling Release</summary>

* Es una distribución de lanzamiento continuo, siendo la antítesis de
Software Versioning, es un sistema de software en constante actualización.
* Utilizar una distribución rolling-release implica tener siempre actualizado los repositorios, lográndose por pequeñas y frecuentes actualizaciones.
</details>

<details>
<summary>Repositorios</summary>

> Cantidad de paquetes aproximada buscada el 2022/05/17.

> Debian posee 59000 paquetes en sus repositorios oficiales.
* Se encuentran repositorios oficiales y no oficiales, AUR, donde hay paquetes incorporados por usuarios.
* AUR cuenta con una cantidad de 74752 paquetes. 
* En los oficiales encontramos 12872 paquetes clasificados en:
    1) core
    2) extra
    3) community
    4) multilib
    5) testing
    6) community-testing
    7) multilib-testing
* Al construir un paquete o votar hay disponibles tres solicitudes que se pueden presentar:
    1) Solicitud de eliminación.
    2) Solicitud de orfandad
    3) Solicitud de unión
</details>

<details>
<summary>Pacman</summary>

> Una dependencia es aquel paquete requerido con antelación para poder concretar una posterior.
* Es un gestor de paquetes permitiendo compilar paquetes y resolver dependencias.
* El mismo fue creado con la intención de terminar con el infierno de dependencias (dependency hell) de RPM en aquel momento.
* Es sólo una pequeña parte del sistema de administración de paquetes debido a que las demás tareas son llevadas a cabo por ABS, Sistema de Construcción de Arch (Arch Build System).
* ABS es un conjunto de herramientas tales como PKGBUILD, makepkg y pacman, donde pacman es completamente independiente pero necesita ser invocado por makepkg para actuar.
*  Un paquete en AUR posee un archivo llamado PKGBUILD, un script de bash, que posee la dirección del código fuente, instrucciones de compilación.
* Los paquetes se compilan por makepkg, que pertenece al paquete Pacman.
</details>

<details>
<summary>Comunidad</summary>

* Con número de 1,980,057 publicaciones en el foro de Arch, un fuerte código de conducta, una diversa cantidad de comunidades internacionales y una wiki que lo tiene todo; vuelven a los Archers protagonistas de este pequeño proyecto.
* En la comunidad se destacan los siguientes roles:
    1) Developer
    2) Trusted User
    3) Arch Tester
    4) Arch Security Tracker
    5) Moderadores de contenido
    6) ArchWiki maintainer
    7) ArchWiki translator
* Existen eventos destinados a la participación masiva de los usuarios en tareas de mantenimiento, entre estos Bug Day y AUR Cleanup Day.
</details>

## ¿Cómo se instala?
<details>
<summary>Preinstalación</summary>

### Soporte
### Requisitos para 64 bits
* Mínimo de 512 MiB de RAM
* Mínimo de 2 GiB de espacio en disco
* Conexión a internet
> También existe soporte para 32 bits y ARM
### Descarga de ISO
* [Descarga](https://archlinux.org/download/)
> La descarga está disponible en forma de torrent, como cliente para gestionarla se usó qBitorrent
### Verificar la integridad
```bash
echo "5934a1561f33a49574ba8bf6dbbdbd18c933470de4e2f7562bec06d24f73839b archlinux-2022.04.05-x86_64.iso" | sha256sum -c
```
> Si el hash coincide correctamente con el otorgado, la integridad no se vio comprometida.
### Verificar la autenticidad
```bash
gpg --keyserver-options auto-key-retrieve --verify archlinux-2022.04.05-x86_64.iso.sig
```
> Si Primary key fingerprint: 4AA4 767B BC9C 4B1D 18AE  28B7 7F2D 434B 9741 E8A coincide, la autenticidad no se vio comprometida
</details>

<details>
<summary>Instalación</summary>

<details>
<summary>Facil</summary>

Usar alguno de los siguientes scripts de instalación:
* [CodigoCristo](https://github.com/CodigoCristo/arcris)
* [Archinstall](https://wiki.archlinux.org/title/Archinstall)

O simplemente importar la VM en:
* [Descarga](https://drive.google.com/drive/folders/1LY-gaM_S8jYhHSml3DpK7-oUq0iXyNk4?usp=sharing)
> Se encuentra en formato .ova y se usó [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
<details>
<summary>Ayuda</summary>

Verificar la integridad
```bash
echo "ab472994bf3f875a8fd262391455bb2f213a143daa6bb9aaf494f6595f2301b8 Arch.ova" | sha256sum -c
```

Solucionar problemas con la resolución de pantalla
```bash
xrandr
xrandr -s <resolucion> #e.g. xrandr -s 1366x768
reboot
```
</details>
</details>

<details>
<summary>Avanzado</summary>

La instalación se realizará haciendo uso de [pacstrap](https://man.archlinux.org/man/pacstrap.8) y [archiso](https://wiki.archlinux.org/title/Archiso). 
```bash
loadkeys la-latin1
localectl list-keymaps
echo KEYMAP=la-latin1 > /etc/vconsole.conf
cat  /etc/vconsole.conf
ls /sys/firmware/efi/efivars
ip link
systemctl restart dhcpcd
fdisk -l
cfdisk
mkfs.ext2 /dev/sda1
mkfs.ext4 /dev/sda2
mkfs.ext4 /dev/sda3
mkswap /dev/sda4
swapon
mount /dev/sda2 /mnt
mkdir /mnt/home
mkdir /mnt/boot
mount /dev/sda1 /mnt/boot
mount /dev/sda3 /mnt/home
pacstrap /mnt base base-devel grub os-prober ntfs-
3g networkmanager gvfs gvfs-afc gvfs-mtp linux linux-firmware
pacstrap /mnt netctl wpa_supplicant dialog
pacstrap /mnt xf86-input-synaptics
genfstab -pU /mnt >> /mnt/etc/fstab
cat /mnt/etc/fstab
arch-chroot /mnt
echo usuario>/etc/hostname
cat /etc/hostname
ls /usr/share/zoneinfo/America
ln -sf /usr/share/zoneinfo/America/Buenos_Aires /etc/localtime
nano /etc/locale.gen
echo LANG=es_AR.UTF-8 > /etc/locale.conf
cat /etc/locale.conf
locale-gen
grub-install /dev/sda
grub-mkconfig -o /boot/grub/grub.cfg
mkinitcpio -p
passwd #usuario_fcyt
useradd -m -g users -G audio,lp,optical,storage,video,wheel,games,power,scanner -
s /bin/bash usuario
passwd usuario #usuario
exit
umount -R /mnt
reboot
```
</details>
</details>

<details>
<summary>Postinstalación</summary>

* Configuración de sudo
> Es tarea del usuario si desea configurar un usuario el sudoers file. Preferentemente usaré root cuando se lo requiera.
* Instalación de principales utilidades y configuración de servicios con systemd
```bash
su root
systemctl start NetworkManager.service
systemctl enable NetworkManager.service
pacman -Syyu
pacman -S neovim htop neofetch git man bat lsd ncdu fzf mc alacritty rofi qtiles feh conky diodon
pacman -S xorg-server xorg-xinit
pacman -S xf86-video-vesa
pacman -S lightdm lightdm-gtk-greeter
systemctl enable lightdm.service
pacman -S xfce4
reboot
```
* Instalar un [helper](https://wiki.archlinux.org/title/AUR_helpers) para manejar paquetes en AUR
```bash
git clone https://aur.archlinux.org/packages/yay
cd yay
makepkg -si
sudo yay -S pamac-aur
```
> yay está desarrollado en go, otra alternativa interesante es paru, desarrollada en Rust

* Instalación de [snap](https://snapcraft.io/docs)
```bash
git clone https://aur.archlinux.com/snapd.git
cd snapd
makepkg -si
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap
sudo snap install brave
```

* Instalación de qtile y [configuración](https://github.com/c05m4r/dotfiles#readme)
```bash
neovim .config/qtile/config.py
```
> configuro archivos con repo de dotfiles, preparo ohmybash, powerline, awesomefonts
</details>

## Recursos
* [ArchWiki](https://wiki.archlinux.org/)
* [Arch Forum](https://bbs.archlinux.org/)
* [Gitlab](https://gitlab.archlinux.org/archlinux)
* [Arch32](https://archlinux32.org/)
* [ArchARM](https://archlinuxarm.org/)
* [Releases](https://archlinux.org/releng/releases/)
* [AUR](https://aur.archlinux.org/)
* [Dotfiles](https://github.com/c05m4r/dotfiles)
* [Distrowatch](https://distrowatch.com/dwres.php?resource=interview-arch) 
* [GUGLER](https://sgd.gugler.com.ar/?ver=trabajo&id_trabajo=229)
* [Telegram Arch Linux Latinoamerica (unofficial)](https://t.me/ArchlinuxLatinoamerica)
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
* Rolling Release
* Repositorios
* Pacman
* Comunidad

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
</details>

<details>
<summary>Avanzado</summary>

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

* Instalación de snap
```bash
#https://snapcraft.io/docs
git clone https://aur.archlinux.com/snapd.git
cd snapd
makepkg -si
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap
sudo snap install brave
```

* Instalación de qtile y configuración
```bash
#https://github.com/c05m4r/dotfiles#readme
#ohmybash, powerline, awesomefonts
#configuro archivos con repo de dotfiles
neovim .config/qtile/config.py
```
</details>

## Recursos
* [ArchWiki](https://wiki.archlinux.org/)
* [Gitlab](https://gitlab.archlinux.org/archlinux)
* [Arch32](https://archlinux32.org/)
* [ArchARM](https://archlinuxarm.org/)
* [Releases](https://archlinux.org/releng/releases/)
* [AUR](https://aur.archlinux.org/)
* [Dotfiles](https://github.com/c05m4r/dotfiles)
* [Distrowatch](https://distrowatch.com/dwres.php?resource=interview-arch) 
* [GUGLER](https://sgd.gugler.com.ar/?ver=trabajo&id_trabajo=229)
* [Telegram Arch Linux Latinoamerica (unofficial)](https://t.me/ArchlinuxLatinoamerica)
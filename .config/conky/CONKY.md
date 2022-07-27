# ¿Cómo configurar conky?

<details>
<summary>Instalación</summary>

> Para [instalar](https://github.com/brndnmtthws/conky/wiki/Installation) conky.
```bash
sudo apt install conky-all
```
> Para descargar [LUA](https://www.lua.org/download.html).

> Comprobar que conky está correctamente instalado.
```bash
conky -v
```
</details>

<details>
<summary>Configuración</summary>

> Crear archivo de configuración.
```bash
mkdir -p ~/.config/conky
conky -C > ~/.config/conky/conky.conf
```
> Establecer la ruta de configuración por defecto.
```bash
conky --config=~/.conky.conf
```
> Para [salvar](https://github.com/brndnmtthws/conky/wiki/Window-Configuration) problemas en WMs agregar al archivo de configuración.
```lua
conky.config = {
    own_window = true,
    own_window_type = 'override',
}
```
> Instalar [conky manager 2](https://github.com/zcot/conky-manager2).
</details>

<details>
<summary>Temas destacados</summary>

* [lipebol](https://github.com/lipebol/config_Conky)
* [Gictorbit](https://github.com/Gictorbit/victorconky)
* [SZinedine](https://github.com/SZinedine/auzia-conky)
* [Kjvthomas](https://github.com/Kjvthomas/sav3d_conky)
</details>

<details>
<summary>Obsoleto/Solucionado</summary>

> Instalar [conky manager](https://github.com/teejee2008/conky-manager)

> .conkyrc debe ir en la ruta ~/
```bash
cp ~/dotfiles/.config/conky/.conkyrc ~/
```
> Dada la nueva version de Conky es necesario convertir el antiguo archivo de configuracion a una nueva sintaxis en LUA. Realizar backup previamente.
```bash
./convert.lua your_config.conf
```
</details>
<!-- Abrir con un procesador de Markdown -->

# Zettabyte File System

## ¿Qué es ZFS?

Es un sistema de archivos y administrador de volúmenes desarrollado por Sun Microsystems (Ahora Oracle) para Solaris OS siendo lanzado en 2006.
ZFS es sólido, escalable y fácil de administrar.

El mismo es soportado en Solaris, OpenSolaris, OpenIndiana, illumos, Joyent SmartOS, OmniOS, FreeBSD, Debian GNU/kFreeBSD systems, NetBSD, OSv y Mac OS con MacZFS.

### Características

* **Pooled Storage - Grupos de Almacenamiento Físico**
    
    Para poder ocuparse de varios dispositivos y ofrecer redundancia de datos, se incorporó el concepto "Administrador de Volumenes", con el fin de ofrecer una representación de un único dispositivo y evitar que los sistemas de archivos tuvieran que modificarse para aprovechar las ventajas de varios dispositivos.
    
    *ZFS elimina del toda la administración de volúmenes*. En vez de tener que crear volúmenes virtualizados, este agrega dispositivos a una agrupación de almacenamiento, donde *el tamaño de los sistemas de archivos crece automáticamente en el espacio asignado a la agrupación de almacenamiento*.

* **Semántica transaccional**

    Los datos se administran mediante la semántica copia por escritura, *Copy On Write*.

    Los datos nunca se sobrescriben y ninguna secuencia de operaciones se compromete ni se ignora por completo.

    Hay garantía de que los datos sincrónicos se escriban antes de la devolución, por lo que nunca se pierden.

    Como desventaja el Copy On Write conlleva una gran fragmentación.

* **Datos de reparación automática y sumas de comprobación**
    
    Todos los datos y metadatos son verificados mediante un algoritmo de *suma de comprobación*.

    Las sumas de comprobación de ZFS se almacenan de forma que estos errores se detecten y haya una recuperación eficaz. 

    Cifrado de 256 bits de los datos en un bloque del sistema de archivos. La suma de comprobación puede ir de la rápida y sencilla fletcher4 (valor predeterminado) a cifrados criptográficamente complejos como SHA256.

    ZFS permite *reparación automática* de datos gracias a la *redundancia de datos* lo que permite recuperar los datos correctos de otra copia si hay un bloque de datos incorrectos.

    Como desventaja, esto implica una gran sobrecarga para el procesador.

* **Snapshots**

    Una instantánea es una copia de sólo lectura de un sistema de archivos o volumen. Las instantáneas se crean rápida y fácilmente. Inicialmente, las instantáneas no consumen espacio adicional en el disco dentro de la agrupación.

    Como los datos de un conjunto de datos activo cambian, la instantánea consume espacio en el disco al seguir haciendo referencia a los datos antiguos.

* **Administración Simplificada**

    Es un FS de distribución jerárquica, herencia de propiedades y administración automática de puntos de montaje y semántica share de NFS, el ZFS facilita la creación y gestión de sistemas de archivos.

    Los sistemas de archivos se convierten en el punto central de control. Los sistemas de archivos son muy sencillos (equivalen a un nuevo directorio), recomendándose crear un sistema de archivos para cada usuario, proyecto, espacio de trabajo. Este diseño permite definir los puntos de administración de forma detallada.

* **RAID Z**

    Esta pretende ser la solución al *write-hole* en  los RAID 5.

    RWH es un escenario de falla, relacionado a la paridad. Ocurre cuando se produce una falla del suministro eléctrico y escritura de fallida de la unidad.

    ZFS utiliza repartos de discos en bandas de RAID de ancho variable. Este diseño solo es posible porque ZFS integra el sistema de archivos y la administración de dispositivos de manera que los metadatos del sistema de archivos tengan suficiente información sobre el modelo de redundancia.    

### Limitaciones

* Se recomienda al menos 8 GB de RAM y una memoria con ECC *(Código Corrector de Errores)*
* Tamaño máximo por volumen 2^128 bytes => 256 trillones de zettabytes de almacenamiento.
* En los nombres de los directorios se permite todo caracter UTF- 8 a excepción de NUL.
* Los directorios pueden tener hasta 2^48 (256 billones) de entradas.
* Longitud máxima en los nombres de archivos de 255 bytes.
* Tamaño máximo de archivo 16 EiB.
* Es case-sensitive.
* No posee límite en la longitud de pathname.
* No posee metadatos del Journaling.
* No posee historial de cambios en archivos.
* No existe un límite para el número de sistemas de archivos o de archivos que puede haber en un sistema de archivos.

### Asignacion de nombres de componentes

Sólo se puede contener caracteres alfanuméricos y caracteres ('_', '-', ':', '.')

* Grupos:

    * Los nombres deben comenzar con una letra.

    * No se permite la secuencia de inicio c[0-9].

    * Son palabras reservadas log, mirror, raidz , raidz1, raidz2, raidz3, spare.

    * Los nombres no pueden contener un signo porcentual '%'.

    * No se permiten los componentes vacíos.


* Conjunto de datos:

    * Nombre genérico de las entidades ZFS siguientes: clones, sistemas de archivos, instantáneas y volúmenes.

    * Los nombres deben comenzar por un carácter alfanumérico.

    * Los nombres no pueden contener un signo porcentual '%'.

    * No se permiten los componentes vacíos.

## Complementario

### ¿Qué es NFS?
    
Network File System (sistema de archivos de red) es un protocolo de nivel de aplicación, según el Modelo OSI.

Es utilizado para sistemas de archivos distribuido en un entorno de red de computadoras de área local.

### ¿Qué es OpenZFS?

El fork de ZFS, OpenZFS dado que ZFS aún mantiene conflictos con su licencia CDDL *(Common Development and Distribution License)* y algunas versiones de GNU Linux no lo tienen como parte de su distribución dado a las incompatibilidades con la licencia GPLv2

### ¿Qué es un LVM - Logical Volume Manager?

### ¿Qué es EVMS - Enterprise Volume Management System?

### ¿Qué es DM - Device Mapper?

### Instalar OpenZFS en Ubuntu

```bash
sudo apt install zfsutils-linux
```
 
### Instalar OpenZFS en Windows 11

Es necesario tener **Windows Pro** y **Windows Insider Program**. Sólo funciona para unidades SSD y la misma no debe ser la que bootea.
* Tener una cuenta de Microsoft vinculada
* Se configura en **WindowsUpdate>WindowsInsiderProgram**, seleccionando el canal **Beta**
* Abrir **Ejecutar** con **WIN + R** y escribir **cmd**
* Ingresar a continuación:
    ```
    Diskpart
    list disk
    list volume
    select disk <numero de unidad>
    clean
    ZFS enable
    Formar Disk <numero de unidad> ZFS
    ZFS Doubler Enable
    ```

O Simplemente instalando:

* [OpenZFS On Windows](https://openzfsonwindows.org/)

## Referencias

* [ZFS - Wikipedia](https://en.wikipedia.org/wiki/ZFS)
* [¿Qué es Oracle Solaris ZFS? - Oracle](https://docs.oracle.com/cd/E26921_01/html/E25823/zfsover-2.html)
* [Versiones de sistema de archivos ZFS - Oracle](https://docs.oracle.com/cd/E26921_01/html/E25823/gjxik.html#scrolltoc)
* [Lab: Introduction to Oracle Solaris 11 ZFS File System - Oracle](https://www.oracle.com/technical-resources/articles/solaris11/s11-intro-zfs.html)
* [An Introduction to the Z File System (ZFS) for Linux - HowToGeek](https://www.howtogeek.com/175159/an-introduction-to-the-z-file-system-zfs-for-linux/)
* [RAID-Z Storage Pool Configuration - Oracle](https://docs.oracle.com/cd/E36784_01/html/E36835/gamtu.html)
* [Requisitos de asignación de nombres de componentes de ZFS - Oracle](https://docs.oracle.com/cd/E26921_01/html/E25823/gbcpt.html#scrolltoc)
* [ZFS: the last word in file systems - Sun](https://web.archive.org/web/20071015014209/http://www.sun.com/2004-0914/feature/)
* [What Stratis learned from ZFS, Btrfs, and Linux Volume Manager - OpenSource.com](https://opensource.com/article/18/4/stratis-lessons-learned)
* [ZFS for Linux - Linuxjournal](https://www.linuxjournal.com/content/zfs-linux)
* [ZFS - Ubuntu](https://wiki.ubuntu.com/ZFS)
* [ZFS On Linux](https://zfsonlinux.org/)
* [Gestión del Administrador de volumen lógico - RedHat](https://access.redhat.com/documentation/es-es/red_hat_enterprise_linux/6/html/logical_volume_manager_administration/index)
* [LVM para torpes](https://blog.inittab.org/administracion-sistemas/lvm-para-torpes-i/)
* [Sistemas de archivos en GNU/Linux - FliSol2019](https://campusvirtual.gugler.com.ar/mod/resource/view.php?id=3792)
* [Comparison of file systems - Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_file_systems)
* [Open ZFS](https://openzfs.org/wiki/Main_Page)
* [Open ZFS On Windows](https://openzfsonwindows.org/)
* [Terminología de ZFS - Oracle](https://docs.oracle.com/cd/E26921_01/html/E25823/ftyue.html#scrolltoc)
* [Linus Torvalds dice que no es prudente utilizar ZFS en Linux](https://blog.desdelinux.net/linus-torvalds-dice-que-no-es-prudente-utilizar-zfs-en-linux/)
* [Copy On Write - Wikipedia](https://es.wikipedia.org/wiki/Copy-on-write)
* [What Is RAID 5 Write Hole (RWH) Protection in Intel® Virtual RAID on CPU (Intel® VROC)?](https://www.intel.com/content/www/us/en/support/articles/000057368/memory-and-storage.html)
* [Network File System - Wikipedia](https://es.wikipedia.org/wiki/Network_File_System)


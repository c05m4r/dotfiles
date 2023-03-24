# Clase 14 Práctica

## Visor de Eventos en Windows

### Consideraciones Previas

1. Abrir el panel **"Ejecutar"** o con el atajo **WIN + R**
2. Ingresar a **"gpedit.msc"** 
3. Dirigirse a: `Directiva Equipo Local > Configuración de Windows > Configuración de Seguridad > Directivas Locales > Directivas de Auditoría`
4. Cambiar auditorías según se lo requiera
5. Para la siguiente actividad se configurarán las directivas: **"Auditar eventos de inicio de sesión"**, **"Auditar eventos de inicio de sesión de cuenta"** y **"Auditar la administración de cuentas"**
### Práctica de Laboratorio 1

#### Identificar intentos fallidos autenticación

1. Cerrar sesión en Windows e ingresar la contraseña de forma incorrecta.
2. Abrir el panel **"Ejecutar"** o con el atajo **WIN + R**
3. Ingresar a **"eventvwr"**
4. Dirigirse a **"Filtrar registro actual"**, sobre el panel vertical de la derecha en **"Acciones"**
5. Preferentemente en el campo **"Palabras clave"**, filtrar según **"Error de auditoría"**
6. Al identificar el evento se observa el **"ID 4625"**, y la **categoría "Logon"**


### Práctica de Laboratorio 2

#### Identificar usuario nuevos

1. Crear un usuario en `Configuración > Cuentas > Familia y otros usuarios > Agregar otro usuario`
2. Abrir el panel **"Ejecutar"** o con el atajo **WIN + R**
3. Ingresar a **"eventvwr"**
4. Dirigirse a **"Filtrar registro actual"**, sobre el panel vertical de la derecha en **"Acciones"**
5. Al agregar miembros se observa el **"ID 4720"**, y la **categoría "User Account Management"**
6. Al quitar miembros se observa el **"ID 4733"**, y la **categoría "Security Group Management"**

### Actividad extra aúlica

#### Exportar registros filtrados

1. Una vez aplicado el filtro, dirigirse a **"Guardar archivo de registro filtrado"**,sobre el panel vertical de la derecha en **"Acciones"**
2. Por defecto se almacenará en **"Documentos"** con la extensión *.evtx*
3. Al abrirlo de podrá encontrar en **"Registros Guardados"** en el Visor de Eventos
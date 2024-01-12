# whatismyip

El siguiente proyecto fue realizado para obtener actualizaciones de la ip pública e informarlo a un usuario en Telegram

## Instalacion

1. Clonar el repositorio

    ``` bash

    git clone https://github.com/c05m4r/dotfiles.git

    ```

2. Dirigirse a la carpeta del proyecto

    ``` bash

    cd ./dotfiles/whatismyip

    ```

3. Crear un entorno virtual

    ``` bash

    python -m venv env

    ```

4. Activar el entorno virtual

    ``` bash

    source env/bin/activate

    ```

5. Instalar paquetes requeridos con pip

    ``` bash

    pip install -r requirements.txt 

    ```

6. Crear una API Key [aquí](https://core.telegram.org/bots#how-do-i-create-a-bot)

7. Agregar la API key de la forma

    <details>

    <summary>Desplegar</summary> 

    ### Windows

    1. Haz clic derecho en "Este equipo" y selecciona "Propiedades" en el menú contextual.
    2. En la ventana de Propiedades del sistema, haz clic en "Configuración avanzada del sistema".
    3. En la ventana Propiedades del sistema, selecciona la pestaña "Opciones avanzadas" y haz clic en 
    4. En la sección "Variables del sistema" o "Variables de usuario", haz clic en "Nuevo".
    5. Ingresa el nombre y el valor de la variable de entorno que deseas agregar y haz clic en "Aceptar".

    O por el comando

    ``` bash

    setx API_KEY <clave>
    setx CHAT_ID @nombrecanal

    ```

    ### POSIX

    ``` bash

    echo -e "API_KEY=<clave>\nCHAT_ID=<user_id>" >> .env

    ```

    </details>

5. Ejecutar el script

    ``` bash

    python main.py

    ```

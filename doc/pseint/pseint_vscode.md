# Escribe pseudocodigo desde VScode

1. Instalar VScode desde https://code.visualstudio.com/ y Pseint desde https://pseint.sourceforge.net/

2. Dentro de VScode. Instalar la extensión Pseudocode.

    1. Presionar CTRL + P
    2. Pegar la siguiente instrucción:
    
        ```
        ext install willumz.generic-pseudocode
        ```

3. Asociar la extensión .psc

    1. Dirigirse al archivo settings.json 

        * Linux
        
            ```
            cd $HOME/.config/Code/User/settings.json
            ```
        
        * Windows

            ```
            cd %APPDATA%\Code\User\settings.json
            ```

    2. Abrir el archivo y pegar el siguiente texto después del primer '{'
    
        ```json
        "files.associations": {
            "*.psc": "pseudocode"
            },
        ```

4. Configuración de la extensión

    1. Crear al archivo

        * Linux
    
            ```
            touch $HOME/.pseudoconfig
            ```
    
        * Windows
    
            ```
            cd C:\Users\{username}\.pseudoconfig
            ```
    
    2. Editar el archivo

        ```json
        { "custom": { "keyword": [ "Algoritmo", "FinAlgoritmo", "Definir", "Escribir", "Leer", "Repetir", "Asignar", "Si", "Entonces", "SiNo", "Fin Si", "Segun", "Hacer", "Fin", "Mientras", "Hasta", "Que", "Para", "Con", "Como", "Paso", "Funcion", "MOD", "Y", "O", "NO", "abs", "trunc", "redon", "raiz", "sen", "cos", "tan", "asen", "acos", "atan", "ln", "exp", "azar", "Longitud", "SubCadena", "Concatenar", "ConvertirANumero", "ConvertirATexto", "Mayusculas", "Minusculas", "PI", "Euler", "Numero", "Numerico", "Real", "Entero", "Logico", "Caracter", "Texto", "Cadena" ] } }
        ```

5. Ejecutar prueba.psc

    1. Presionar CTRL + SHIT + P
    2. Escribir "Toggle Terminal"
    3. Ejecutar la siguiente instrucción
    
        ```
        pseint prueba.psc
        ```

    > Para Linux se debe crear un enlace simbólico a /usr/bin de la forma
    
    ```
    cd $HOME/<directorio_pseint>/pseint/bin
    sudo ln -s $(realpath ./pseint) /usr/bin/pseint
    ```
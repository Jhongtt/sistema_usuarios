# Sistema de Gestion de Usuarios

Este proyecto lo hice para aprender a organizar un proyecto en Python de forma
profesional. La idea es simple, es un programa que corre en la terminal y te
permite registrar usuarios, listarlos y buscarlos. Nada de interfaz grafica,
todo por consola.

## Como crear el entorno virtual

Primero hay que crear el entorno virtual. Esto sirve para que las librerias
que instalemos no afecten otros proyectos de Python en el computador.
Es como tener una carpeta separada solo para este proyecto.

Para crearlo se escribe esto en la terminal:

python -m venv venv

Eso crea una carpeta llamada venv dentro del proyecto con todo lo necesario.

## Como activar el entorno virtual

Despues de crearlo hay que activarlo. Si no lo activas, Python no va a usar
las librerias del proyecto sino las del sistema.

En Windows se activa asi:

venv\Scripts\activate

Cuando esta activo se ve el texto (venv) al inicio de la terminal.
Eso significa que ya esta funcionando correctamente.

## Como instalar las dependencias

Las dependencias son las librerias externas que necesita el proyecto.
En este caso solo se usa una que se llama python-dotenv y sirve para
leer el archivo .env con las variables de entorno.

Para instalarlas se usa este comando:

pip install -r requirements.txt

Ese comando lee el archivo requirements.txt y instala todo lo que esta listado
ahi automaticamente.

## Como ejecutar el proyecto

Con el entorno virtual activado y las dependencias instaladas, el proyecto
se ejecuta con este comando:

python main.py

Eso abre el menu en la terminal donde puedes elegir que hacer.

## Que hace cada archivo

main.py
Este es el archivo principal. Tiene el menu que se muestra en pantalla y
llama a las funciones de los otros modulos segun lo que elija el usuario.
Es el punto de entrada del programa.

gestor.py
Este archivo maneja toda la logica de los usuarios. Tiene las funciones para
registrar un usuario nuevo, listar todos los usuarios guardados y buscar
por nombre o por correo. Guarda los usuarios en una lista mientras el
programa esta corriendo.

validaciones.py
Antes de guardar cualquier dato este archivo se asegura de que la informacion
sea correcta. Valida que el nombre no este vacio y solo tenga letras, que la
edad sea un numero entre 1 y 120, y que el correo tenga un formato valido
con @ y punto. Si algo esta mal lanza un error con un mensaje claro.

settings.py
Este archivo se encarga de leer las variables del archivo .env usando
python-dotenv. Las variables quedan disponibles para usarlas en cualquier
parte del proyecto sin tener que escribir los valores directamente en el codigo.

## Variables de entorno

Las variables de entorno son valores de configuracion que se guardan por fuera
del codigo. Esto es util porque si el proyecto lo usa otra persona solo cambia
el archivo .env sin tocar nada del codigo.

El archivo .env tiene esto:

APP_NAME=Sistema Usuarios
APP_VERSION=1.0
ADMIN_USER=admin

Ese archivo no se sube a GitHub porque puede tener informacion sensible.
En cambio se sube un archivo .env.example con los mismos nombres pero
sin los valores reales para que cualquiera sepa que variables necesita configurar.

## Estructura del proyecto

sistema_usuarios/
    app/
        config/
            settings.py
        usuarios/
            gestor.py
            validaciones.py
    .env
    .env.example
    main.py
    requirements.txt
    README.md

## Dependencias

python-dotenv: permite leer las variables del archivo .env de forma sencilla
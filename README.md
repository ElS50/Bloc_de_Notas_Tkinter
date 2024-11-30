# Bloc_de_Notas_Tkinter
### Crear un Bloc de Notas con Tkinter

## Inicio de Sesión con Tkinter y SQLite
#### Crear un sistema básico de autenticación que incluya:
#### Registro de usuarios (crear una cuenta).
#### Inicio de sesión (autenticación).
#### Persistencia de datos con SQLite.

## Requisitos
### El alumno necesita:
#### Entender conceptos básicos de bases de datos.
#### Tener instalada la biblioteca sqlite3 (incluida en Python).

## Estructura del Registro de Usuario
### Ventana de inicio:
#### Dos botones: Iniciar Sesión y Registrarse.
#### Ventana de registro:
#### Permite al usuario ingresar nombre, correo electrónico y contraseña.
#### Ventana de inicio de sesión:
#### Verifica las credenciales y da acceso al Bloc de Notas.
### Bloc de Notas:
#### Solo accesible después de iniciar sesión.

## Guía Paso a Paso
### a) Configuración de la base de datos
Crear una base de datos SQLite para almacenar usuarios.
### b) Ventana de inicio
Una ventana principal con dos opciones: Iniciar Sesión y Registrarse.
### c) Registro de usuarios
Una ventana para que el usuario cree una cuenta.
### d) Inicio de sesión
Una ventana que verifica las credenciales del usuario.
### e) Integrar el Bloc de Notas
Conecta el Bloc de Notas como ventana principal tras iniciar sesión.

## Extensiones del Proyecto
#### Olvidé mi contraseña: Implementa una funcionalidad para recuperar o restablecer contraseñas.
#### Sesión persistente: Guarda la información del usuario logueado usando cookies o archivos locales.
#### Multisesión: Permite que varios usuarios usen la aplicación con su configuración personalizada.
#### Historial de archivos por usuario: Crea una tabla en la base de datos para guardar los archivos editados por cada usuario.

## Beneficios para el Alumno
#### Refuerza conceptos de bases de datos y manejo de errores.
#### Aprende a conectar la interfaz gráfica con la lógica del backend.
#### Gana experiencia creando aplicaciones completas y funcionales.

### Con esta guía, el alumno tendrá un desafío interesante y aprenderá habilidades esenciales para el desarrollo de software.

## Objetivo del Proyecto
### Crear una aplicación GUI que permita al usuario:

#### Escribir texto.
#### Guardar texto en un archivo.
#### Abrir archivos existentes.
#### Editar el texto.
#### Personalizar la experiencia con opciones adicionales.

## Funcionalidades Básicas
### a) Crear el área de texto
#### Usa ScrolledText para un área de texto con barra de desplazamiento.
#### Haz que el texto sea editable.

### b) Guardar archivo
#### Usa el módulo filedialog para abrir un cuadro de diálogo de "Guardar".
#### Guarda el contenido del texto en el archivo seleccionado.

### c) Abrir archivo
#### Usa filedialog para abrir archivos.
#### Carga el contenido del archivo en el área de texto.

## Funcionalidades Adicionales
#### Funciones de edición, copiar, Cortar y Pegar: Usa métodos del widget "Text"
#### Hacer un Boton para cada función.
#### Agrega una barra de menú con opciones.
#### Búsqueda: Permite buscar una palabra en el texto.
#### Reemplazo: Reemplaza una palabra por otra:
#### Permite al usuario elegir entre temas claros y oscuros.
#### Muestra en tiempo real cuántas palabras tiene el texto.

## Funcionalidades Avanzadas
#### Exportar como PDF: Usa bibliotecas como reportlab para generar archivos PDF.

    pip install reportlab

#### Autoguardado: Guarda automáticamente el contenido cada cierto tiempo.
#### Historial de archivos recientes: Mantén un registro de los últimos archivos abiertos/guardados.
#### Deshacer y Rehacer: Usa los métodos edit_undo y edit_redo del widget Text.

## Retos para el Alumno
#### Implementa todas las funcionalidades básicas y avanzadas.
#### Agrega un botón de ayuda que muestre información sobre cómo usar el Bloc.
#### Crea un sistema de configuración donde el usuario pueda personalizar el tamaño de fuente, colores, etc.
#### Empaca el proyecto como ejecutable usando PyInstaller.




import sqlite3
import hashlib

def hashear_contrasena(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def inicio_sesion():
    nombre_usuario = input("Digite su nombre: ")
    contrasena = input("Digite su contraseña: ")

    #Hashear la contraseña ingresada
    contrasena_hashed = hashear_contrasena(contrasena)

    # Conectar a la base de datos
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    # Verificar si el nombre de usuario y la contraseña existen
    cursor.execute("""
    SELECT * FROM usuarios WHERE nombre_usuario = ? AND contrasena = ?
    """, (nombre_usuario, contrasena_hashed))
    
    usuario = cursor.fetchone()  # Obtener el primer registro que coincida

    if usuario:
        print("Inicio de sesión exitoso.")
    else:
        print("Usuario o contraseña incorrectos.")

    conexion.close()
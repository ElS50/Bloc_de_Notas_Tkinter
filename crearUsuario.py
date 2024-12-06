import sqlite3
import hashlib

from crear_base_usuarios import iniciar_bd;

from inicioSesion import inicio_sesion;

def hashear_contrasena(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario;
        self.contrasena = contrasena;

    def __str__(self):
        return f"Usuario: {self.nombre_usuario}, contraseña:{self.contrasena}"

#funcion para crear usuario
def contrasena_crear():

    nombre_usuario = input("Digite su nombre: ");
    
    while True:
        contrasena = input("Contraseña: ")

        if len(contrasena) >= 8:
            break
        else:
            print("La conraseña debe tener 8 caracteres")
    
    contrasena_hashed = hashear_contrasena(contrasena)

    #conexion a la base de datos

    try:
        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()
        cursor.execute("""
        INSERT INTO usuarios (nombre_usuario, contrasena) VALUES (?, ?)
        """, (nombre_usuario, contrasena_hashed))
        conexion.commit()
        print("Usuario creado exitosamente.")
    except sqlite3.IntegrityError:
        print("El nombre de usuario ya existe. Intente con otro.")
    finally:
        conexion.close()

    # Inicializar base de datos

# iniciar_bd()

# #contrasena_crear()

# inicio_sesion()

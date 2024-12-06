import sqlite3
import hashlib
import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Bloc de Notas")
root.geometry("400x300")  # Tamaño de la ventana (ancho x alto)

tk.Label(root, text="Bienvenido", font=("Arial", 14), fg="white", bg="grey").pack(pady=20) 



class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario;
        self.contrasena = contrasena;

    def __str__(self):
        return f"Usuario: {self.nombre_usuario}, contraseña:{self.contrasena}"

#funcion para crear usuario
def contrasena_crear():

    #nombre_usuario = input("Digite su nombre: ");
    
    while True:
        #contrasena = input("Contraseña: ")

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





###################################
#inicio sesion
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

# contrasena_crear()

# inicio_sesion()


# Iniciar el loop de la aplicación
root.mainloop()
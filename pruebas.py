import hashlib
import sqlite3
import tkinter as tk
from crear_base_usuarios import iniciar_bd

# Función para encriptar la contraseña
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Crear la ventana principal
root = tk.Tk()
root.title("Bloc de Notas")
root.geometry("400x300")  # Tamaño de la ventana (ancho x alto)

tk.Label(root, text="Bienvenido", font=("Arial", 14), fg="white", bg="grey").pack(pady=20) 

usuario_nuevo = tk.Entry(root, font=("Arial", 14))
usuario_nuevo.pack(pady=10)

def registro():
    agregar_usuario = usuario_nuevo.get()  # Obtener el texto escrito
    contrasena = contrasenanueva.get()  # Obtener el texto escrito
    conn = sqlite3.connect('usuarios_mensajes.db')
    cursor = conn.cursor()

    conn.close()


tk.Button(root, text="Registrar", command=registro).pack()


iniciar_bd()


root.mainloop()
# Iniciar el loop de la aplicación
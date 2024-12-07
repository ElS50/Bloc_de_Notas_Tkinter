import sqlite3
import hashlib
import tkinter as tk
from tkinter import messagebox
from app_principal import abrir_ventana_principal  # Importar la ventana principal

# Crear la base de datos y tabla si no existen
def crear_base_datos():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)
    conn.commit()
    conn.close()

crear_base_datos()

# Encriptar contraseñas
def encriptar_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Registrar un usuario
def registrar_usuario(username, password):
    try:
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, encriptar_password(password)))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

# Validar un usuario
def validar_usuario(username, password):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM usuarios WHERE username = ?", (username,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        return resultado[0] == encriptar_password(password)
    return False

# Función para registrar un usuario desde el formulario
def registrar_desde_formulario():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:  # Validar que los campos no estén vacíos
        if registrar_usuario(username, password):
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
            root.destroy()  # Cerrar la ventana de inicio de sesión
            abrir_ventana_principal()  # Llamar a la ventana principal desde el archivo importado
        else:
            messagebox.showerror("Error", "El nombre de usuario ya existe.")
    else:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")

# Función para validar un usuario desde el formulario
def validar_desde_formulario():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:  # Validar que los campos no estén vacíos
        if validar_usuario(username, password):
            root.destroy()  # Cerrar la ventana de inicio de sesión
            abrir_ventana_principal()  # Llamar a la ventana principal desde el archivo importado
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
    else:
        messagebox.showerror("Error", "Por favor, completa todos los campos.")

# Crear la ventana principal de inicio de sesión
root = tk.Tk()
root.title("Bloc de Notas")
root.resizable(False, False)  # Bloquea el tamaño en ambas direcciones
root.geometry("400x300")  # Tamaño de la ventana (ancho x alto)
root.configure(bg="black")

# Etiqueta de bienvenida
tk.Label(root, text="Inicio de Sesion", font=("Arial", 14), fg="white", bg="black").pack(pady=10)

# Etiquetas y campos de entrada para el usuario
tk.Label(root, text="Nombre de usuario:", bg="black", fg="white").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Contraseña:", bg="black", fg="white").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

btn_validate = tk.Button(root, text="Iniciar Sesión", bg="red", fg="white", command=validar_desde_formulario)
btn_validate.pack(pady=5)

# Crear un marco rojo con fondo negro y bordes
marco = tk.Frame(root, bg="black", bd=2, relief="solid", highlightbackground="red", highlightcolor="red", highlightthickness=2)
marco.pack(pady=10, padx=20)  # Espaciado alrededor del marco

# Botones para registrar y validar con fondo rojo y texto blanco
btn_register = tk.Button(marco, text="Registrar", bg="red", fg="white", command=registrar_desde_formulario)
btn_register.pack(side="left", padx=10, pady=10)  # Alinear a la izquierda, con margen horizontal y vertical

btn3 = tk.Button(marco, text="Recuperar Contraseña", bg="red", fg="white")
btn3.pack(side="left", padx=10, pady=10)



# Iniciar el loop de la aplicación
root.mainloop()


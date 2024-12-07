import tkinter as tk


# Variable global para la referencia de la ventana
registrar_usuario = None

# Función para abrir la ventana de recuperación
def ventana_registro():
    global registrar_usuario

    # Si la ventana ya está abierta, no hacemos nada
    if registrar_usuario:
        print("La ventana ya está abierta.")
        return

    # Crear una nueva ventana
    registrar_usuario = tk.Toplevel()
    registrar_usuario.title("REGISTRAR USUARIO NUEVO")
    registrar_usuario.geometry("300x400")
    registrar_usuario.resizable(False, False)  # Bloquea el tamaño en ambas direcciones
    registrar_usuario.configure(bg="black")

    # Función para manejar el cierre de la ventana
    def cerrar_ventana():
        global registrar_usuario
        registrar_usuario.destroy()
        registrar_usuario = None
        print("Ventana cerrada.")

    # Configurar el botón de cerrar manualmente
    tk.Button(registrar_usuario, text="Cerrar", command=cerrar_ventana).pack(pady=10)

    # Configurar el protocolo WM_DELETE_WINDOW para cerrar la ventana
    registrar_usuario.protocol("WM_DELETE_WINDOW", cerrar_ventana)

    print("Ventana de recuperación abierta.")

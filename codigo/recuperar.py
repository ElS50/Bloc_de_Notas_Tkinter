import tkinter as tk


# Variable global para la referencia de la ventana
ventana_recuperacion_abierta = None


# Función para abrir la ventana de recuperación
def ventana_recuperacion():
    global ventana_recuperacion_abierta

    # Si la ventana ya está abierta, no hacemos nada
    if ventana_recuperacion_abierta:
        print("La ventana ya está abierta.")
        return

    # Crear una nueva ventana
    ventana_recuperacion_abierta = tk.Toplevel()
    ventana_recuperacion_abierta.title("Recuperar Contraseña")
    ventana_recuperacion_abierta.geometry("300x400")
    ventana_recuperacion_abierta.resizable(False, False)  # Bloquea el tamaño en ambas direcciones
    ventana_recuperacion_abierta.configure(bg="black")

    # Función para manejar el cierre de la ventana
    def cerrar_ventana():
        global ventana_recuperacion_abierta
        ventana_recuperacion_abierta.destroy()
        ventana_recuperacion_abierta = None
        print("Ventana cerrada.")

    # Configurar el botón de cerrar manualmente
    tk.Button(ventana_recuperacion_abierta, text="Cerrar", command=cerrar_ventana).pack(pady=10)

    # Configurar el protocolo WM_DELETE_WINDOW para cerrar la ventana
    ventana_recuperacion_abierta.protocol("WM_DELETE_WINDOW", cerrar_ventana)

    print("Ventana de recuperación abierta.")

import tkinter as tk

def abrir_ventana_principal():
    # Crear la ventana principal
    nueva_ventana = tk.Tk()
    nueva_ventana.title("Bloc de Notas")
    nueva_ventana.geometry("400x300")
    nueva_ventana.configure(bg="black")

    # Contenido de la ventana principal
    tk.Label(nueva_ventana, text="¡Bienvenido a la App!", font=("Arial", 16), bg="black", fg="white").pack(pady=20)
    
   
    # Iniciar el loop de la ventana
    nueva_ventana.mainloop()

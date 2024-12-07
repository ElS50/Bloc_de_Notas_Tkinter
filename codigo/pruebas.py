import tkinter as tk

# Crear ventana principal
root = tk.Tk()
root.title("Ejemplo de botones alineados")
root.geometry("400x200")
root.configure(bg="gray")

# Crear un marco blanco con bordes
marco = tk.Frame(root, bg="white", bd=2, relief="solid")  # bd: tamaño del borde, relief: estilo del borde
marco.pack(pady=20, padx=20)  # Espaciado alrededor del marco

# Añadir los botones dentro del marco
btn1 = tk.Button(marco, text="Botón 1")
btn1.pack(side="left", padx=10, pady=10)  # Alinear a la izquierda, con margen horizontal y vertical

btn2 = tk.Button(marco, text="Botón 2")
btn2.pack(side="left", padx=10, pady=10)

btn3 = tk.Button(marco, text="Botón 3")
btn3.pack(side="left", padx=10, pady=10)

# Iniciar el loop principal
root.mainloop()

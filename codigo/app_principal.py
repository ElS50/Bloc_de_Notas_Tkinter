import tkinter as tk
from tkinter import filedialog, scrolledtext

def abrir_ventana_principal():
    # Crear la ventana principal
    nueva_ventana = tk.Tk()
    nueva_ventana.title("Bloc de Notas")
    nueva_ventana.geometry("800x800")
    nueva_ventana.configure(bg="black")


    #_________________ área de texto ________________
    # Contenido de la ventana principal
    tk.Label(nueva_ventana, text="¡Bienvenido a tu espacio de escritura!", font=("Arial", 16), bg="black", fg="white").pack(pady=20)

    # Crear un marco para organizar el área de texto
    area_texto = tk.Frame(nueva_ventana, bg="black")
    area_texto.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Crear el widget ScrolledText (editable por defecto) con fondo gris
    scrolled_text = scrolledtext.ScrolledText(area_texto, wrap=tk.WORD, width=80, height=30, bg="#7d0101", fg="white")
    scrolled_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Insertar texto inicial opcional
    scrolled_text.insert(tk.INSERT, "Escribe aquí...")
        



    #__________________ Guardar en archivo_____________

    def guardar_archivo():
        # Abrir cuadro de diálogo para guardar
        archivo = filedialog.asksaveasfilename(
            title="Guardar archivo",
            defaultextension="",  # Extensión predeterminada
            filetypes=[("Archivos de texto", "*.txt"), ("Markdown", "*.md"), ("Archivos Python", "*.py"), ("Todos los archivos", "*.*")]
        )
        if archivo:  # Si se seleccionó un archivo
            with open(archivo, "w", encoding="utf-8") as f:
                contenido = scrolled_text.get("1.0", tk.END)  # Obtener el contenido del área de texto
                f.write(contenido)  # Escribir el contenido en el archivo
            print(f"Archivo guardado en: {archivo}")



    #_____________________Cargar archivo_________________
    def abrir_archivo():
        # Abrir cuadro de diálogo para seleccionar archivo
        archivo = filedialog.askopenfilename(
            title="Abrir archivo",
            filetypes=[("Archivos de texto", "*.txt"), ("Markdown", "*.md"), ("Archivos Python", "*.py"), ("Todos los archivos", "*.*")]
        )
        if archivo:  # Si se seleccionó un archivo
            with open(archivo, "r", encoding="utf-8") as f:
                contenido = f.read()  # Leer el contenido del archivo
                scrolled_text.delete("1.0", tk.END)  # Limpiar área de texto
                scrolled_text.insert(tk.INSERT, contenido)  # Insertar contenido
            print(f"Archivo cargado: {archivo}")

    # Crear un marco rojo con fondo negro y bordes
    marco = tk.Frame(area_texto, bg="black", bd=2, relief="solid", highlightbackground="red", highlightcolor="red", highlightthickness=2)
    marco.pack(pady=10, padx=20)  # Espaciado alrededor del marco

    # Botón para guardar el archivo
    btn_guardar = tk.Button(marco, text="Guardar archivo", bg="red", fg="white", command=guardar_archivo)
    btn_guardar.pack(side="left", padx=10, pady=10)  # Alinear a la izquierda, con margen horizontal y vertical

    # Botón para abrir archivo
    btn_abrir = tk.Button(marco, text="Abrir archivo", bg="red", fg="white", command=abrir_archivo)
    btn_abrir.pack(side="left", padx=10, pady=10)



    # Iniciar el loop de la ventana

    nueva_ventana.mainloop()

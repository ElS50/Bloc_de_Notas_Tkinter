import tkinter as tk
from tkinter import filedialog, scrolledtext


# Crear la ventana principal
nueva_ventana = tk.Tk()
nueva_ventana.title("Bloc de Notas")
nueva_ventana.geometry("800x800")
nueva_ventana.configure(bg="black")


#_________________ área de texto ________________
# Contenido de la ventana principal
tk.Label(nueva_ventana, text="¡Bienvenido a la App!", font=("Arial", 16), bg="black", fg="white").pack(pady=20)

#Crear un marco para organizar el área de texto
area_texto = tk.Frame(nueva_ventana, bg="black")
area_texto.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Crear el widget ScrolledText (editable por defecto)
scrolled_text = scrolledtext.ScrolledText(area_texto, wrap=tk.WORD, width=80, height=30)
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

# Botón para guardar el archivo
btn_guardar = tk.Button(area_texto, text="Guardar archivo", command=guardar_archivo)
btn_guardar.pack(pady=10)


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

# Botón para abrir archivo
btn_abrir = tk.Button(area_texto, text="Abrir archivo", command=abrir_archivo)
btn_abrir.pack(pady=10)


# def abrir_ventana_principal():
    

    # Iniciar el loop de la ventana

nueva_ventana.mainloop()

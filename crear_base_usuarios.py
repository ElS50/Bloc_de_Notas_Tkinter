import sqlite3

# Conexión o creación de la base de datos
conn = sqlite3.connect("mi_base_de_datos.db")  # Se crea si no existe

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear una tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL,
    email TEXT UNIQUE
)
""")

print("Base de datos y tabla creadas con éxito.")

# Cerrar la conexión
conn.commit()  # Guardar cambios
conn.close()

import sqlite3

# Conectar a la base de datos (esto crea el archivo si no existe)
def iniciar_bd():
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()

    # Crear la tabla de usuarios (id, nombre_usuario, contrasena)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_usuario TEXT UNIQUE,
            contrasena TEXT)
    ''')

    conexion.commit()
    conexion.close()

    

#print("Base de datos creada y tabla 'usuarios' configurada.") Se descomenta solo si hay un error en la base

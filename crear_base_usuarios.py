import sqlite3

conexion = sqlite3.connect('usuarios.db')

cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT NOT NULL,
        contrasena TEXT NOT NULL         
    )
''')

conexion.commit()

print("Base de datos creada y tabla 'usuarios' configurada.")
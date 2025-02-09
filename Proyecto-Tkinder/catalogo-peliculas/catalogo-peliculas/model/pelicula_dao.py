from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(60),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )'''

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

        titulo = 'Crear Registro'
        mensaje = 'Se creo la tabla en la base de datos'
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya está creada'
        messagebox.showwarning(titulo,mensaje)

def borrar_tabla():
    conexion = ConexionDB()
    sql = 'DROP TABLE peliculas'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

        titulo = 'Borrar Registro'
        mensaje = 'La tabla de la base de datos se borro con éxito'
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = 'Borrar Registro'
        mensaje = 'No existe tabla para borrar'
        messagebox.showerror(titulo,mensaje)
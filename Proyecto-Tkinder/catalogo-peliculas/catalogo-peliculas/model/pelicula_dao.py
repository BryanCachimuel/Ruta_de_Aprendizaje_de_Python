from .conexion_db import ConexionDB

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

    conexion.cursor.execute(sql)
    conexion.cerrar()

def borrar_tabla():
    conexion = ConexionDB()
    sql = 'DROP TABLE peliculas'

    conexion.cursor.execute(sql)
    conexion.cerrar()
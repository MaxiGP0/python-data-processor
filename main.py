import os

# Archivo donde vamos a guardar los datos (nuestra "base de datos" simple)
ARCHIVO_DATOS = "alumnos.txt"

def cargar_datos():

    """Lee el archivo .txt y carga los datos en un diccionario."""
    alumnos = {}
    # Si el archivo no existe, devolvemos un diccionario vacio.
    if not os.path.exists(ARCHIVO_DATOS):
        return alumnos

    # Abrimos el archivo en forma de lectura.
    with open(ARCHIVO_DATOS, 'r') as archivo:

        # Recorremos las lineas.
        for linea in archivo:

            # Limpiamos el salto de linea y separamos por comas.
            datos = linea.strip().split(',')

            if len(datos) == 4:

                # Guardamos en el diccionario usando el ID como clave.
                id_alumno, nombre, edad, estado = datos
                

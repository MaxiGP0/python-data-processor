import os

# Archivo donde vamos a guardar los datos (nuestra "base de datos" simple)
ARCHIVO_DATOS = "alumnos.txt"


# cargar_datos: void -> Dict,
# cargar_datos, lee el archivo "alumnos.txt" y retorna un diccionario con todos los alumnos, usando su ID como clave.
def cargar_datos():
    
    """Lee el archivo .txt y carga los datos en un diccionario."""
    alumnos = {}

    # Si el archivo no existe, devolvemos un diccionario vacío
    if not os.path.exists(ARCHIVO_DATOS):
        return alumnos

    # Abrimos el archivo .txt en forma de lectura.
    with open(ARCHIVO_DATOS, 'r') as archivo:

        # Recorremos las lineas. 
        for linea in archivo:
            
            # Limpiamos el salto de línea y separamos por comas.
            datos = linea.strip().split(',')

            # Comprobamos que hayan 4 datos (el id del alumno, su nombre, su edad y su estado).
            if len(datos) == 4:

                # Cambio de variables para mas comodidad.
                id_alumno, nombre, edad, estado = datos
                
                # Guardamos en el diccionario usando el ID como clave
                alumnos[id_alumno] = {
                    'nombre': nombre, 
                    'edad': edad, 
                    'estado': estado
                }

    # Retornamos el diccionario que guarda a todos los alumnos.
    return alumnos


# guardar_datos: Dict -> void
# guardar_datos, toma un diccionario de alumnos, y sobreescribe el archivo .txt con los datos actuales del diccionario.
def guardar_datos(alumnos):

    # Abrimos el archivo en forma de escritura.
    with open(ARCHIVO_DATOS, 'w') as archivo:

        # Recorremos la el diccionario de alumnos.
        for id_alumno, info in alumnos.items():
            
            # Volvemos a armar la línea separada por comas.
            linea = f"{id_alumno},{info['nombre']},{info['edad']},{info['estado']}\n"
            archivo.write(linea)
            
# agregar_alumno: Dict -> Dict
# agregar_alumno, toma un diccionario de alumnos, y agrega uno a al diccionario.
def agregar_alumno(alumnos):

    # Le solicitamos al usuario el ID del alumno.
    print("\n--- Agregar Nuevo Alumno ---")
    id_alumno = input("Ingrese ID único: ")

    # Comprobamos su existencia.
    if id_alumno in alumnos:
        print("¡Error! Ese ID ya existe.")
        return

    # Solicitamos al usuario todos los datos del alumno.
    nombre = input("Nombre completo: ")
    edad = input("Edad: ")
    estado = input("Estado (Activo/Inactivo): ")

    # Lo guardamos en el diccionario.
    alumnos[id_alumno] = {'nombre': nombre, 'edad': edad, 'estado': estado}
    print(f"¡Alumno {nombre} agregado con éxito!")
    

def buscar_alumno(alumnos):
    """Busca un alumno por su ID en el diccionario (búsqueda instantánea)."""
    print("\n--- Buscar Alumno ---")
    id_buscado = input("Ingrese el ID del alumno a buscar: ")
    
    if id_buscado in alumnos:
        info = alumnos[id_buscado]
        print("\n--- Resultados ---")
        print(f"Nombre: {info['nombre']}")
        print(f"Edad: {info['edad']}")
        print(f"Estado: {info['estado']}")
        print("------------------")
    else:
        print("No se encontró ningún alumno con ese ID.")

def menu_principal():
    """Maneja la interfaz de consola del programa."""
    # Cargamos los datos a la memoria RAM apenas arranca el programa
    base_de_datos = cargar_datos()
    
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE ALUMNOS ===")
        print("1. Agregar un registro")
        print("2. Buscar un registro")
        print("3. Guardar y Salir")
        
        opcion = input("Elegí una opción (1-3): ")
        
        if opcion == '1':
            agregar_alumno(base_de_datos)
        elif opcion == '2':
            buscar_alumno(base_de_datos)
        elif opcion == '3':
            guardar_datos(base_de_datos)
            print("Datos guardados. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intentá de nuevo.")

# Punto de entrada del script
if __name__ == "__main__":
    menu_principal()

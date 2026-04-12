Sistema de Gestión de Alumnos

Este es un script de Python sencillo y funcional diseñado para gestionar registros de alumnos mediante una interfaz de línea de comandos (CLI). El sistema permite realizar operaciones básicas de base de datos (CRUD) utilizando un archivo de texto plano (.txt) como persistencia de datos.

🚀 Características

Persistencia de Datos: Los datos se guardan automáticamente en un archivo alumnos.txt, lo que permite cerrar el programa sin perder la información.

Gestión Completa:


- Agregar: Registro de nuevos alumnos con ID único, nombre, edad y estado.

- Buscar: Localización rápida de alumnos por su ID.

- Eliminar: Borrado de registros existentes de la memoria.

- Reportes Estadísticos: Genera un resumen en tiempo real que incluye:


  - Total de alumnos registrados.

  - Conteo de alumnos activos e inactivos.

  - Promedio de edad de los alumnos registrados.


🛠️ Requisitos

- Python 3.x: El script utiliza funciones estándar de Python y no requiere librerías externas.

- Sistema Operativo: Windows, macOS o Linux.

📋 Estructura del Archivo de Datos

El programa utiliza un archivo llamado alumnos.txt. Los datos se almacenan en formato CSV (valores separados por comas) con la siguiente estructura:

ID,Nombre,Edad,Estado

Ejemplos:

- 101,Juan Perez,20,Activo

- 102,Maria Garcia,22,Inactivo

💻 Uso

- Clonar o descargar el archivo .py en tu computadora.

- Abrir una terminal en la carpeta donde se encuentra el archivo.

- Ejecutar el programa con el siguiente comando:

python nombre_de_tu_archivo.py

Navegar por el menú: Utiliza los números del 1 al 5 para seleccionar la acción que deseas realizar.

Para asegurar que los cambios se guarden permanentemente, siempre utiliza la Opción 5 (Guardar y Salir) para cerrar el programa.

📂 Estructura del Código

El script está organizado en funciones modulares para facilitar su mantenimiento:

- cargar_datos(): Inicializa el sistema leyendo el archivo de texto.
    
- guardar_datos(): Escribe la información actual de la memoria al archivo físico.

- agregar_alumno(): Maneja la entrada de nuevos datos y validación de IDs.

- buscar_alumno(): Filtra el diccionario por clave (ID).

- eliminar_alumno(): Elimina entradas del diccionario de datos.

- generar_reporte(): Procesa las estadísticas (conteo y promedios).

- main(): Contiene el bucle principal y la lógica de la interfaz de usuario.

📝 Notas de desarrollo

- El sistema incluye validaciones básicas para evitar errores si el archivo de datos no existe al inicio.

- Se ha implementado una limpieza de strings (strip()) y manejo de minúsculas/mayúsculas para que el reporte estadístico sea más preciso independientemente de cómo el usuario escriba el estado.

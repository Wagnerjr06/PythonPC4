def contar_lineas_codigo(ruta_archivo):
    """Cuenta las líneas de código de un archivo .py, excluyendo comentarios y líneas en blanco."""
    try:
        # Verifica que el archivo tenga la extensión .py
        if not ruta_archivo.endswith('.py'):
            print("El archivo no tiene la extensión .py. No se puede procesar.")
            return
        
        # Abre y lee el archivo
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
        
        # Filtra las líneas que no son comentarios ni están en blanco
        lineas_codigo = [linea for linea in lineas if linea.strip() and not linea.strip().startswith('#')]
        
        # Muestra el número de líneas de código
        print(f"Número de líneas de código (sin comentarios ni líneas en blanco): {len(lineas_codigo)}")
    
    except FileNotFoundError:
        print("El archivo no se pudo encontrar. Verifique la ruta e inténtelo de nuevo.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")


def menu():
    """Función principal que solicita la ruta del archivo y llama a contar_lineas_codigo."""
    while True:
        ruta_archivo = input("Ingrese la ruta del archivo .py (o 'salir' para terminar): ")
        
        if ruta_archivo.lower() == 'salir':
            print("Saliendo del programa.")
            break
        
        contar_lineas_codigo(ruta_archivo)


if __name__ == "__main__":
    menu()

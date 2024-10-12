def guardar_tabla_multiplicar(n):
    """Guarda en un archivo la tabla de multiplicar del número n."""
    nombre_archivo = f"tabla-{n}.txt"
    with open(nombre_archivo, "w") as archivo:
        for i in range(1, 11):
            archivo.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla de multiplicar del {n} guardada en {nombre_archivo}.")


def leer_tabla_multiplicar(n):
    """Lee el archivo con la tabla de multiplicar del número n y la muestra por pantalla."""
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")


def mostrar_linea_tabla(n, m):
    """Muestra la línea m de la tabla de multiplicar del número n."""
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, "r") as archivo:
            lineas = archivo.readlines()
            if 1 <= m <= len(lineas):
                print(lineas[m - 1].strip())
            else:
                print(f"La tabla solo tiene {len(lineas)} líneas. No hay línea {m}.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")


def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Guardar tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Mostrar línea específica de una tabla")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                n = int(input("Ingrese un número entero entre 1 y 10: "))
                if 1 <= n <= 10:
                    guardar_tabla_multiplicar(n)
                else:
                    print("El número debe estar entre 1 y 10.")
            except ValueError:
                print("Debe ingresar un número válido.")
        
        elif opcion == "2":
            try:
                n = int(input("Ingrese un número entero entre 1 y 10: "))
                if 1 <= n <= 10:
                    leer_tabla_multiplicar(n)
                else:
                    print("El número debe estar entre 1 y 10.")
            except ValueError:
                print("Debe ingresar un número válido.")
        
        elif opcion == "3":
            try:
                n = int(input("Ingrese un número entero entre 1 y 10 (n): "))
                m = int(input("Ingrese un número entero entre 1 y 10 (m): "))
                if 1 <= n <= 10 and 1 <= m <= 10:
                    mostrar_linea_tabla(n, m)
                else:
                    print("Ambos números deben estar entre 1 y 10.")
            except ValueError:
                print("Debe ingresar un número válido.")
        
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()

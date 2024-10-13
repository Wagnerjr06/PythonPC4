import csv
import sqlite3
from datetime import datetime

# Función para obtener el tipo de cambio desde SQLite
def obtener_tipo_cambio(fecha, db_path='base.db'):
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Consulta para obtener el tipo de cambio por fecha
    cursor.execute("SELECT venta FROM sunat_info WHERE fecha = ?", (fecha,))
    tipo_cambio = cursor.fetchone()

    # Si no se encuentra el tipo de cambio, devuelve None
    if tipo_cambio is None:
        return None
    return tipo_cambio[0]

# Función para procesar las ventas y convertir precios a soles
def procesar_ventas(archivo_ventas, db_path='base.db'):
    ventas = []

    # Leer el archivo CSV
    with open(archivo_ventas, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        next(lector_csv)  # Saltar la cabecera si existe

        for fila in lector_csv:
            fecha_compra, producto, cantidad, precio_dolares = fila
            cantidad = int(cantidad)
            precio_dolares = float(precio_dolares)

            # Convertir la fecha en el formato adecuado
            fecha_formateada = datetime.strptime(fecha_compra, "%Y-%m-%d").strftime("%Y-%m-%d")

            # Obtener el tipo de cambio de la base de datos
            tipo_cambio = obtener_tipo_cambio(fecha_formateada, db_path)

            if tipo_cambio:
                # Calcular el precio en soles
                precio_total_dolares = precio_dolares * cantidad
                precio_total_soles = precio_total_dolares * tipo_cambio
                ventas.append((producto, precio_total_dolares, precio_total_soles))
            else:
                print(f"No se encontró tipo de cambio para la fecha: {fecha_formateada}")

    # Mostrar los resultados
    for venta in ventas:
        producto, precio_total_dolares, precio_total_soles = venta
        print(f"Producto: {producto}, Precio en dólares: {precio_total_dolares:.2f}, Precio en soles: {precio_total_soles:.2f}")

# Ruta del archivo de ventas
archivo_ventas = 'ventas.csv'

# Ejecutar la función para procesar las ventas
procesar_ventas(archivo_ventas)

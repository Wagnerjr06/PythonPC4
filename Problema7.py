import requests
import sqlite3
from pymongo import MongoClient
import json
from datetime import datetime, timedelta

# URL del API de SUNAT para obtener el tipo de cambio
url_api = "https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha={fecha}"

# Función para obtener el tipo de cambio de una fecha específica
def obtener_tipo_cambio(fecha):
    url = url_api.format(fecha=fecha)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Conexión a SQLite y creación de la tabla
def crear_tabla_sqlite():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT,
            compra REAL,
            venta REAL
        )
    ''')
    conn.commit()
    conn.close()

# Función para insertar los datos en SQLite
def insertar_en_sqlite(fecha, compra, venta):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)", (fecha, compra, venta))
    conn.commit()
    conn.close()

# Conexión a MongoDB
def conectar_mongo():
    client = MongoClient("mongodb://localhost:27017/")
    db = client['sunat_db']
    collection = db['sunat_info']
    return collection

# Función para insertar los datos en MongoDB
def insertar_en_mongo(collection, fecha, compra, venta):
    data = {
        'fecha': fecha,
        'compra': compra,
        'venta': venta
    }
    collection.insert_one(data)

# Función principal para obtener y almacenar los datos del 2023
def obtener_y_almacenar_datos():
    # Crear tabla SQLite si no existe
    crear_tabla_sqlite()
    
    # Conexión a MongoDB
    collection_mongo = conectar_mongo()
    
    # Fechas del 2023
    fecha_inicio = datetime(2023, 1, 1)
    fecha_fin = datetime(2023, 12, 31)
    
    fecha_actual = fecha_inicio
    
    while fecha_actual <= fecha_fin:
        fecha_str = fecha_actual.strftime('%Y-%m-%d')
        datos = obtener_tipo_cambio(fecha_str)
        
        if datos:
            compra = float(datos['compra'])
            venta = float(datos['venta'])
            print(f"Fecha: {fecha_str}, Compra: {compra}, Venta: {venta}")
            
            # Insertar en SQLite
            insertar_en_sqlite(fecha_str, compra, venta)
            
            # Insertar en MongoDB
            insertar_en_mongo(collection_mongo, fecha_str, compra, venta)
        
        # Avanzar un día
        fecha_actual += timedelta(days=1)

# Mostrar los datos de la tabla en SQLite
def mostrar_datos_sqlite():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sunat_info")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    conn.close()

# Ejecutar el código
obtener_y_almacenar_datos()

# Mostrar datos almacenados en SQLite
print("\nDatos almacenados en SQLite:")
mostrar_datos_sqlite()

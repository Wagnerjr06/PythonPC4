import requests
import zipfile
import os

def descargar_imagen(url, nombre_archivo):
    try:
        respuesta = requests.get(url, stream=True)
        if respuesta.status_code == 200:
            with open(nombre_archivo, 'wb') as file:
                for chunk in respuesta.iter_content(1024):
                    file.write(chunk)
            print(f"Imagen descargada como: {nombre_archivo}")
        else:
            print(f"No se pudo descargar la imagen. Código de estado: {respuesta.status_code}")
    except requests.RequestException as e:
        print(f"Error al descargar la imagen: {e}")

def crear_zip(nombre_archivo, nombre_zip):
    try:
        with zipfile.ZipFile(nombre_zip, 'w') as zipf:
            zipf.write(nombre_archivo)
        print(f"Imagen comprimida en: {nombre_zip}")
    except Exception as e:
        print(f"Error al crear el archivo zip: {e}")

def extraer_zip(nombre_zip, ruta_extraccion):
    try:
        with zipfile.ZipFile(nombre_zip, 'r') as zipf:
            zipf.extractall(ruta_extraccion)
        print(f"Archivo extraído en: {ruta_extraccion}")
    except Exception as e:
        print(f"Error al extraer el archivo zip: {e}")

def main():
    url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    nombre_imagen = "imagen_descargada.jpg"
    nombre_zip = "imagen_comprimida.zip"
    ruta_extraccion = "./imagen_extraida"
    
    # Crear directorio de extracción si no existe
    if not os.path.exists(ruta_extraccion):
        os.makedirs(ruta_extraccion)

    # Descargar la imagen
    descargar_imagen(url_imagen, nombre_imagen)

    # Comprimir la imagen en un archivo zip
    crear_zip(nombre_imagen, nombre_zip)

    # Extraer el archivo zip
    extraer_zip(nombre_zip, ruta_extraccion)

if __name__ == "__main__":
    main()

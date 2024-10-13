import csv

def procesar_temperaturas(archivo_entrada, archivo_salida):
    temperaturas = []

    with open(archivo_entrada, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            fecha, temperatura = fila
            temperaturas.append(float(temperatura))

    temp_promedio = sum(temperaturas) / len(temperaturas)
    temp_maxima = max(temperaturas)
    temp_minima = min(temperaturas)

    with open(archivo_salida, 'w') as archivo_resumen:
        archivo_resumen.write(f"Temperatura promedio: {temp_promedio:.2f}°C\n")
        archivo_resumen.write(f"Temperatura máxima: {temp_maxima:.2f}°C\n")
        archivo_resumen.write(f"Temperatura mínima: {temp_minima:.2f}°C\n")

archivo_entrada = 'temperaturas.txt'
archivo_salida = 'resumen_temperaturas.txt'

procesar_temperaturas(archivo_entrada, archivo_salida)

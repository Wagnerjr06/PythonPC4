import requests

def obtener_precio_bitcoin():
    try:
        respuesta = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        respuesta.raise_for_status()
        datos = respuesta. json()

        precio_bitcoin = datos['bpi']['USD']['rate_float']
        return precio_bitcoin
    except requests.RequestException as e:
        print(f"Error al consultar el precio de Bitcoin: {e}")
        return None
    
def main():
    try:
        n = float(input("Ingrese la cantidad de Bitcoins que posee: "))
        precio_bitcoin = obtener_precio_bitcoin()
        if precio_bitcoin is not None:
            valor_total = n * precio_bitcoin
            print(f"El valor de {n} Bitcoins es: ${valor_total:,.4f} USD")
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == '__main__':
    main()    

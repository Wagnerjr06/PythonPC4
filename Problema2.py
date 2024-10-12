import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()

    fuentes_disponibles = figlet.getFonts()

    fuente_seleccionada = input("Ingrese el nombre de la fuente (deje en blanco para seleccionar una aleatoria): ")
    if fuente_seleccionada == "":
        fuente_seleccionada = random.choice(fuentes_disponibles)
        print(f"Se ha seleccionada aleatoriamente la fuente: {fuente_seleccionada}")

    try:
        figlet.setFont(font=fuente_seleccionada)
    except:
        print(f"Fuente '{fuente_seleccionada}' no es válida. Usando una fuente aleatoria.")
        fuente_seleccionada = random.choice(fuentes_disponibles)
        figlet.setFont(font=fuente_seleccionada)
        print(f"Se ha seleccionada aleatoriamente la fuente: {fuente_seleccionada}")

    texto = input("Ingrese el texto que desea convertir en arte ASCII: ")

    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()


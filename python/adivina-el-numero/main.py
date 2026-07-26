'''
Adivina el Número:

La máquina elige un número del 1 al 100; tú adivinas y te dice
"mayor" o "menor" hasta acertar. Al final muestra cuántos intentos
usaste.

Antonio de Jesus Zamorano Mendez - 26 de Julio del 2026
'''

import os
import random

os.system("clear")

while True:
    limite = input("Elige el número máximo a adivinar (Ejemplo: Si escribes 27, el número a adivinar estará entre 0 y 27): ")
    try:
        limite = int(limite)
        if limite > 0:
            break
        else:
            print("El número debe ser mayor a 0.")
    except ValueError:
        print("Solo se admiten números. Reintente.")

numero = random.randint(0, limite)

def main():
    intentos = 0
    while True:
        entrada = input("escriba un número: ")
        intentos += 1

        try:
            entrada = int(entrada)

            if numero == entrada:
                print(f"¡Felicidades! has acertado el número en {intentos} intentos.")
                break
            elif numero > entrada:
                print("El número a adivinar es mayor.")
            else:
               print("El número a adivinar es menor.")
        except ValueError:
            print("Solo se admiten números. Por favor reintente.")

main()

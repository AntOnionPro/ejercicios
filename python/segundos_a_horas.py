'''
Conversión y operadores.

Escribe un programa que pida al usuario un número de segundos (entero) y lo convierta a formato horas:minutos:segundos.
Por ejemplo, si el usuario ingresa 3661, debe imprimir 1:1:1.

Antonio de Jesus Zamorano Mendez - 07/08/26
'''

import os

os.system("cls")

horas = 0

def segundosAHoras(segundos):
    horas = segundos // 3600

    segundos_restantes = segundos % 3600

    minutos = segundos_restantes // 60

    segundos_finales = segundos_restantes % 60

    return f"{horas:02d}:{minutos:02d}:{segundos_finales:02d}"

print("==================================================================")
print(" Bienvenido, por favor ingrese una cantidad de segundos entera:\n              ('salir' para detener la ejecución)")
print("==================================================================")

while True:
    segundos = input("Cantidad: ")

    if segundos == "salir":
        break

    try:
        segundos = int(segundos)

        print(f"Tiempo en Formato HH:MM:SS: {segundosAHoras(segundos)}")
    except ValueError:
        print("Ingrese un monto válido, por favor.")





import os


os.system("cls")


def factorial():
    os.system("cls")
    while True:
        print("---------------------")
        print(" Eligió opción 1 (Escriba 'salir' para abandonar).")
        print("---------------------")
        numero = input("Por favor introduzca un número: ")
        resultado = 1
        try:
            numero = int(numero)
            while numero > 1:
                resultado = resultado * (numero)
                numero -= 1
            print(f"El resultado es: {resultado}")
        except ValueError:
            if numero == "salir":
                break
            print("Por favor, introduzca un número.")

def aplicar_iva():
    os.system("cls")
    while True:
        print("---------------------")
        print(" Eligió opción 2 (Escriba 'salir' para abandonar).")
        print("---------------------")
        subtotal = input("Por favor introduzca un número (subtotal): ")
        try:
            subtotal = int(subtotal)
            while subtotal > 0:
                iva = input("Por favor introduzca un iva a aplicar: ")
                try:
                    iva = int(iva)
                    print(f"El resultado es: ${subtotal + (subtotal * iva / 100)} mxn.")
                    break
                except ValueError:
                    print("Por favor, introduzca un número y que sea mayor a 0.")
        except ValueError:
            if subtotal == "salir":
                break
            print("Por favor, introduzca un número y que sea mayor a 0.")


while True:
    os.system("cls")
    print("------------------------------")
    print(" Bienvenido, Elige una opción (Escriba 'salir' para abandonar):")
    print("------------------------------")

    print("(1) Función que recibe un número y devuelve su factorial.")
    print("(2) Función que recibe monto y el IVA a aplicar; devuelve su total.")
    opcion = input("Opción elegida: ")

    try:
        opcion = int(opcion)
        match opcion:
            case 1:
                factorial()
            case 2:
                aplicar_iva()
            case _:
                print("Esa opción no está en la lista. Reintente.")
    except ValueError:
        if opcion == "salir":
            break
        print("\nLa opción debe ser un número. Reintente.")





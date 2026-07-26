/*
Adivina el Número:

La máquina elige un número del 1 al número que indiques; tú adivinas y te dice
"mayor" o "menor" hasta acertar. Al final muestra cuántos intentos
usaste.

Antonio de Jesus Zamorano Mendez - 26 de Julio del 2026
*/

using System;

class AdivinaElNumero 
{
    private static int intentos = 0;

    static void Main()
    {
        Console.Clear();

        int limite = PedirLimite();
        int numero = Random.Shared.Next(0, limite + 1);       

        Console.WriteLine($"Estoy pensando un número entre 0 y {limite}.");
        Console.WriteLine("Escribe 'salir' si te deseas rendir.\n");

        Jugar(numero);
    }

    static int PedirLimite()
    {
        while (true)
        {
            Console.Write("Elige el número máximo a adivinar: ");
            string? entrada = Console.ReadLine();

            if (int.TryParse(entrada, out int limite) && limite > 0)
            {
                return limite;
            }

            Console.WriteLine("Necesito un número mayor a 0. Reintenta.");   
        }
    }

    static void Jugar(int numero)
    {
        while (true)
        {
            Console.Write("Escribe un número: ");
            string? entrada = Console.ReadLine();

            if (entrada?.Trim().ToLower() == "salir")
            {
                Console.WriteLine($"El número era {numero} y usaste {intentos} intentos.");
                return;
            }

            intentos++;

            if (!int.TryParse(entrada, out int adivinanza))
            {
                Console.WriteLine("Solo se admiten números. Por favor reintente.");
                continue;
            }

            if (adivinanza == numero)
            {
                Console.WriteLine($"\nAcertaste en {intentos} intentos.");
                return;
            }

            Console.WriteLine(numero > adivinanza ? "El número a adivinar es mayor." : "El número a adivinar es menor.");
        }
    }

}










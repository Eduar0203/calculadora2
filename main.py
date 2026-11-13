
import math

print("===== CALCULADORA EN PYTHON =====")

while True:
    print("\nSeleccione una operación:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Raíz cuadrada (√)")
    print("6. Potencia (^)")
    print("7. Porcentaje (%)")
    print("8. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "8":
        print("Gracias por usar la calculadora.")
        break

    if opcion in ["1", "2", "3", "4", "6", "7"]:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "1":
            resultado = num1 + num2
            print("Resultado:", resultado)

        elif opcion == "2":
            resultado = num1 - num2
            print("Resultado:", resultado)

        elif opcion == "3":
            resultado = num1 * num2
            print("Resultado:", resultado)

        elif opcion == "4":
            if num2 != 0:
                resultado = num1 / num2
                print("Resultado:", resultado)
            else:
                print("Error: No se puede dividir entre cero.")

        elif opcion == "6":
            resultado = num1 ** num2
            print("Resultado:", resultado)

        elif opcion == "7":
            resultado = (num1 * num2) / 100
            print("Porcentaje:", resultado)

    elif opcion == "5":
        num1 = float(input("Ingrese el número: "))

        if num1 >= 0:
            resultado = math.sqrt(num1)
            print("Raíz cuadrada:", resultado)
        else:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")

    else:
        print("Opción no válida. Intente nuevamente.")




print("=== CALCULADORA BÁSICA ===")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("\nSeleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingrese una opción: ")

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
        print("No se puede dividir entre cero.")

else:
    print("Opción no válida.")

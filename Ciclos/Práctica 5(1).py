numero = int(input("Ingrese un número entero positivo: "))
if numero <= 0:
    print("El número debe ser positivo.")
else:
    for numero in range(1,numero + 1):
        if numero %2 != 0:
            print(numero, end = ",")
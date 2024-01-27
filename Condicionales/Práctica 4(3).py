edad = int(input("Ingrese la edad del cliente: "))

if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 110
else:
    precio = 190

print("El precio de la entrada es:", precio)
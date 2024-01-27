palabra= input("Ingrese su palabra ")
palabra = palabra.replace(" ", "").lower()
if palabra == palabra[::-1]:
    print("La palabra es un palíndromo")
else:
    print("La palabra no es un palíndromo")
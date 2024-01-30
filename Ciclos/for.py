palabra=input("Ingrese una palabra: ")
contador_vocales=0
for letra in palabra:
    if letra.lower() in "aeiou":
        contador_vocales +=1
print("La palabra", palabra, "tiene", contador_vocales, "vocales")

'''#FOR US
suma=0
for num in range(1,11):
    if num %2==0:
        suma +=num
print("La suma es", suma)'''
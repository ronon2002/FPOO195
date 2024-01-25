
#Practica2: Sintaxis Python

#1. Comentarios

#soy  un comentario de 1 linea

'''soy un
comentario
de
varias lineas
'''



#2. Cadenas

''''print('soy una cadena')
print("soy otra cadena")

a= ' mi banda \n favorita es'
b= " grupo marrano"
print(a,b) #esta deja un espacio
print(a+b) #esta las pega tal cual, sin espacio

#contar los caracteres incluye espacios
print(len(a))


print(b[2:5]) #imprime las posiciones situando rangos.
print(b[:5])  #imprime desde el inicio hasta la posicion 5.
print(b[2:])  #imprime desde la posicion 2 hasta el final.
'''
#3. Variables.

'''x=int(3)
y=str("3")
z=float(3.2)

print(type(x))
print(type(y))

print(type(x))
print(type(y))
print(type(z))
import random
numero=random.randrange(1,15)
print(numero)
print(numero)'''

#4. Solicitud de datos.

'''var1= input("introduce cualquier dato: ")

var2= str(input("introduce cadenas: "))
var3= int(input("introduce solo enteros: "))
var4= float(input("introduce numeros decimales: "))

print("los datos que introduciste son: ", var1,var2,var3,var4)'''

#5. Booleans, Operadores de comparacion y Operadores logicos.

'''print(10>9)
print(10==9)
print(10<9)
print(10>=9)
print(10!=9)
print(10<=9)'''

#logicos

x=1
print(x<5 and x<10)
print(x<5 or x<10)
print(not(x<5 and x<10))

#Para operaciones binarias
print(x<5 & x<10)
print(x<5 | x<10)
print(not(x<5 & x<10))
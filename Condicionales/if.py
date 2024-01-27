'''z=4
if z % 2 == 0:
    print("z es par")'''
    
#if else
'''z=int(input("Ingresa un número entero: "))
if z % 2 == 0:
    print("z es par")
else:
    print("z es impar")'''

#if elif else
room="bed"
area=14.0
if room == "bed" and area > 11:
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else:
    print("looking around elsewhere.")
    
    if area > 15:
        print("big place!")
    else:
        print("pretty small.")
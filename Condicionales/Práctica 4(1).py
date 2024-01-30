contrasena_guardada=input("Ingresa la contraseña nueva: ")

contrasena_usuario=input("Confirma tu contraseña: ")

if contrasena_guardada.lower() == contrasena_usuario.lower():
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")
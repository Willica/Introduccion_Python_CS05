name = input("Cual es tu nombre: ")
# Remover espacios en blanco si el usuario los introduce por error
# name = name.strip()
# Primera letra con mayuscula
# name = name.title()
# Reduciendo los codigos anteriores
name = name.strip().capitalize()
# Separar nombre y apellido
nombre, apellido = name.split(" ")
# Primera forma de encadenar caracteres
print(f"mi nombre es {nombre}")
# Segunda forma de encadenar caracteres
print("mi nombre es " + apellido)
# Otra forma vista desde la documentación de Python
print("mi nombre es ",end="")
print(nombre)
# name = input("Nombre: ")
"""
# VERSION 1

#Se abre el archivo en modo añadir
file = open("names.txt","a")
#Se escribe sobre el archivo con un salto de linea
file.write(f"{name}\n")
#Se cierra el archivo de modo de guardar los cambios
file.close()

"""
"""
# VERSION 2

# Al salir de la identacion el archivo se cierra
#Se abre el archivo en modo añadir
with open("names.txt","a") as file:
    #Se escribe sobre el archivo con un salto de linea
    file.write(f"{name}\n")
"""
"""
############################################################################################################
Respecto a la version 1 se mejora en cuanto a utilizar la funcion with dado que permite ahorrar la linea de
.close que en ocasiones esta puede ser olvidada, entonces cuando se sale de la identacion el programa guarda
el archivo
############################################################################################################
"""
"""
# VERSION 3

#Se abre el archivo en forma de lectura
with open("names.txt","r") as file:
    #Se leen todas las lineas del archivo y se genera una lista con lo que haya en dicho documento
    lines = file.readlines()
#Ciclo for para iterar en la lista lines
for line in lines:
    #Imprime en pantalla lo de la lista
    #print(f"Hello, {line}",end= "")
    print(f"Hello, {line.rstrip()}")
"""
"""
############################################################################################################
La version 3 propone la apertura del archivo .txt en formato de escritura
############################################################################################################
"""
"""
# VERSION 4

with open("names.txt","r") as file:
    for line in file:
        print(f"Hello, {line.rstrip()}")
"""
"""
############################################################################################################
La mejora con respecto a la version 3 de este programa es que no es necesario generar la variable lines
puesto que files de por si es una lista que puede ser recorrida
############################################################################################################
"""
"""
# VERSION 5
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"Hello, {name}")
"""
# VERSION 6

with open("names.txt") as file:
    for line in sorted(file):
        print(f"Hello, {line.rstrip()}")

# min 25.04
"""
############################################################################################################
La mejora de la version 6 con respecto a la version 5 radica en que no es necesaria generar una lista
que que luego se ordena, más bien es posible que la lista "file" sea reorganizada.
############################################################################################################
"""
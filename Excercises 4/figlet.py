"""
Implementar un programa que acepte 0 o 2 argumentos.
1) Si no se ingresa argumento a la hora de ejecutar el codigo python figlet.py entonces se asigna
una fuente random.
2) Si se ingresan 2 argumento uno debe ser -f o --font y el otro debe ser el nombre de la fuente.

Al ejecutar el programa e introducir el texto deseado a convertir deberia imprimir en pantalla
el texto con la fuente deseada (si se estipulo). Por el contrario si se asigna solo un parametro previo
a correr el programa, se debe arrojar un error o salir directamente del programa.
"""

#Libreria aleatoria
import random
#Importar librerias sys
import sys
#Desde pyfiglet importar Figlet
from pyfiglet import Figlet

figlet = Figlet()
lista = figlet.getFonts()

def main():
    #Se obtiene la lista de las fuentes disponibles
    print(conversion())

def conversion():
    if len(sys.argv)==1:
        text = input("Input: ")
        f = random.choice(lista)
        figlet.setFont(font=f)
        return figlet.renderText(text)
    elif (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in lista)==True:
        text = input("Input: ")
        #f corresponde al nombre de la fuente ingresado
        f = sys.argv[2]
        #Se aplica el nombre de la fuente
        figlet.setFont(font=f)
        #Se imprime el texto convertido
        return figlet.renderText(text)
    else:
        #Se sale del programa
        sys.exit("Invalid usage")

main()
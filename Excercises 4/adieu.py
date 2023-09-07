#Importar libreria
import inflect
#Comando extraido de documentacion
p = inflect.engine()
#Lista de nombres
nombres = []
#Bucle infinito
while True:
    try:
        #Lectura de teclado 
        nombre = input("Name: ")
        #Añadir elemento a lista
        nombres.append(nombre)
    except EOFError:
        #Abreviacion "," y "and" proporionado por la libreria invocada
        mylist = p.join(nombres)
        #Imprimir en pantalla
        print(f"Adieu, adieu, to {mylist}")
        #Salir del bucle
        break


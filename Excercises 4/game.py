#Importar libreria random
import random
#Lista vacia
numeros = []
#Lectura de teclado de nivel
while True:
    try:
        level = int(input("Level: "))
        #Inicializacion de i
        i = 1
        #Bucle que genera el vector de numeros de 1 hasta n
        while i <= level:
            numeros.append(i)
            i += 1
        #Eleccion de un numero random de la lista anterior
        numero_random = random.choice(numeros)
        break
    #Solucion a posibles errores
    except (ValueError,IndexError):
        ...

while True:
    try:
        #Lectura de teclado de suposición
        n = int(input("Guess: "))
        #Condicionales
        if n > numero_random:
            print("El numero es mas pequeño")
        elif 0 < n < numero_random:
            print("El numero es mas mas grande")
        elif n == numero_random:
            print("Es correcto")
            break
        else:
            pass
    #Solucion a error
    except ValueError:
        ...





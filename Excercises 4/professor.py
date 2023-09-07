"""
- Proponer al usuario un nivel "n". Si el usuario no ingresa como entrada
1, 2 o 3, el programa deberia proponer nuevamente al usuario que ingrese el
nivel.
- Generar de manera random 10 probelmas matematicos en formato "X + Y = ",
donde X e Y o pueden ser negativos y deben contener n digitos. No se soportan
otras operaciones distinta a la suma.
- Proponer al ususario resolver los probelmas. Si la respuesta es incorrecta
el programa deberia dar como salida EEE y se deberia proponer ingresar
nuevamente al usuario ingresar la respuesta, si el usuario ingresa 3 veces una
respuesta incorrecta el programa debe dar la respuesta correcta.
- El programa al finalizar los 10 problemas debe arrojar como salida el score
obtenido.
"""
import random

#Función principal
def main():
    #Llamado a funciones
    numeros = generate_integer(get_level())
    #Inicializaciones
    score = 0
    x = numeros[0]
    y = numeros[1]
    i = 0
    error = 0
    #Bucle para generar 10 operaciones
    while i < len(x):
        try:
            #Lectura de telcado de resultado de resultado
            resultado = int(input(f"{x[i]} + {y[i]} = "))
            #Condicional
            if resultado == x[i] + y[i]:
                #Incremento de score
                score = score + 1
                #Incremento de variable i para salir del bucle cuando i == 10
                i += 1
            else:
                #Arroja el error en caso de que no se cumpla condicion anterior
                raise Exception("Error")
        #Manejo de error en caso de que se introduzca algo distinto a un numero entero
        except (ValueError,IndexError,Exception):
            print("EEE")
            #Incremento del error
            error = error + 1
            #Condicional para arrojar respuesta correcta
            if error == 3:
                    print(f"{x[i]} + {y[i]} = {x[i]+y[i]}")
                    #Se re-inicializa el error
                    error = 0
                    #Se aumenta la variable i
                    i += 1
    #Se imprime el score una vez se sale del bucle
    print(f"Score: {score}")

#Funcion para obtener nivel        
def get_level():
    while True:
        try:
            #Pide nivel al usuario
            level = int(input("Level: "))
            return level
        #Corrige errores en caso de ingresar algo que no sea un numero entero
        except (ValueError, IndexError, TypeError):
            pass

#Funcion para generar los numeros
def generate_integer(level):
    while True:
        try:
            x = []
            y = []
            i = 0
            if 1<=level<=3:
                #Del 0 al 9
                if level == 1:
                    while i < 10: 
                        num_x = random.randint(0,9)
                        num_y = random.randint(0,9)
                        x.append(num_x)
                        y.append(num_y)
                        i += 1
                    return x,y
                #Del 10 al 99
                elif level == 2:
                    while i < 10: 
                        num_x = random.randint(10,99)
                        num_y = random.randint(10,99)
                        x.append(num_x)
                        y.append(num_y)
                        i += 1
                    return x,y
                #Del 100 al 999
                elif level == 3:
                    while i < 10: 
                        num_x = random.randint(100,999)
                        num_y = random.randint(100,999)
                        x.append(num_x)
                        y.append(num_y)
                        i += 1
                    return x,y
            else:
                raise TypeError("El numero no se encuentra en el rango")
        except TypeError:
            level = get_level()
            ...

#Se ejecuta solo si se ejecuta el programa principal
if __name__ == "__main__":
    main()
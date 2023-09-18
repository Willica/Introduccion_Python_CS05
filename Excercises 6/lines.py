"""
Crear un programa que lea lineas de codigo.
- Si la linea empieza con # no se cuenta
- Esta vacia no se considera
- Si la linea empieza con " se contara las lineas que se encuentran denrtro y se descontaran
"""
#Se importa libreria sys
import sys
#Se intenta lo siguiente
try:
    #Se separa lo de sys.argv[1] para conocer el nombre y extension del archivo
    nombre,extension = sys.argv[1].split(".")
    #Si la extension es .py y el largo es igual a 2 se ejecuta la linea de codigo
    if extension == "py" and len(sys.argv) == 2:
        #Se abre el archivo y se guarda cuando se sale de la identidad
        with open(sys.argv[1]) as file:
            #Se inicializan las variables contadoras
            linea_codigo = 0
            linea_comentario = 0
            #Para linea en el archivo
            for line in file:
                #Se quitan los espacios presentes en line
                line = line.lstrip()
                #Si la linea comienza con # o esta vacia entonces se corre la linea de codigo
                if line.startswith("#") == True or not line:
                    #Se agrega a la variable contadora de comentarios +1
                    linea_comentario = linea_comentario + 1
                #Se agrega +1 a la variable de codigos totales
                linea_codigo = linea_codigo + 1
        #La resta indica la cantidad de lineas de codigo
        lineas_total_codigo = linea_codigo - linea_comentario
        #Se imprime en pantalla la cantidad de lineas de codigo
        print(f"Lineas de codigo: {lineas_total_codigo}")
    #Si la extension es distinta de .py entonces se arroja el error y se sale del programa
    elif extension != "py" or not extension:
        sys.exit("Not a Python file")
    #Si el largo de sys.argv[] es mayor que 2 entonces se arroja el error y se sale del programa
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
#Si falla con Value error se arroja el siguien error
except (ValueError, FileNotFoundError):
    sys.exit("File does not exist")
#Si falla con el IndexError se arroja el siguiente error
except IndexError:
    sys.exit("Too few command-line arguments")
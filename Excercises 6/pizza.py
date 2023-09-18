#Se importan librerias
from tabulate import tabulate
import csv
import sys 

try:
    nombre,extension = sys.argv[1].split(".")
    if len(sys.argv) == 2 and extension == "csv":
        #Se genera una lista vacia
        lista = []
        #Se abre el archivo .csv
        with open(sys.argv[1]) as file:
            #Se lee y almacena en reader las lineas del archivo .csv
            reader = csv.reader(file)
            #Ciclo for para recorrer reader
            for row in reader:
                #Se agrega a la lista la linea leida por row en reader
                lista.append(row)
        #Se imprime la tabla
        print(tabulate(lista[1:],lista[0] ,tablefmt="grid"))
    #Si el largo de sys.argv es mayor que uno entonces:
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    #Condicional si no entra en los otros condicionales
    else:
        sys.exit("Not a CSV file")
#Error en caso que archivo no exista
except (FileNotFoundError,ValueError):
    sys.exit("File does not exist")
#Error si no se ingresa nada en la linea de comando
except IndexError:
    sys.exit("Too few command-line arguments")

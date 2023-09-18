#Se importan librerias
import sys
import os
from PIL import Image, ImageOps
#Se intenta
try:
    #Se separa en una lista el nombre y la extension del archivo
    name_exte1 = os.path.splitext(sys.argv[1])
    name_exte2 = os.path.splitext(sys.argv[2])
    #Se genera una lista con las extension admitidas
    formato = [".png",".jpg",".jpeg"]
    #Condicional para abrir el archivo
    if (len(sys.argv) == 3) and ((name_exte1[1] in formato) and (name_exte2[1] in formato)):
        try:
            #Se abre imagen a editar
            with Image.open(sys.argv[1]) as entrada:
                #Condicional de extensiones
                if name_exte1[1] == name_exte2[1]:
                    #Se abre imagen que se desea superponer
                    shirt = Image.open("shirt.png")
                    #Se obtienen las dimensiones de la imagen que se desea superponer
                    size = shirt.size
                    #Se escala la imagen a editar a escala de imagen a superponer
                    salida = ImageOps.fit(entrada,size)
                    #Se pega sobre la imagen de entrada la imagen a superponer
                    salida.paste(shirt,shirt)
                    #Se cierra shirt
                    shirt.close()
                    #Se guarda la imagen en formato .jpeg
                    salida.save(sys.argv[2])
                #Si no se cumple condicional se arroja error
                else:
                    sys.exit("Input and output have different extensions")
        #Si no existe el archivo que se abre entonces se imprime el argumentos de sys.exit
        except FileNotFoundError:
            sys.exit("Input does not exist")
    #Condicional en caso de ingresar mas de la cantidad de argumentos admitidos
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    #Condicional en caso de ingresar extensiones erroneas
    else:
        sys.exit("Invalid output")
#Condicional en caso de no ingresar la cantidad de argumentos admitidos
except IndexError:
    sys.exit("Too few command-line arguments ")

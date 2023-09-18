#Libreria que acepta parametros en linea de comando
import sys
#Desde PIL se importa la libreria image que permite interactuar con archivos con extension de imagen
from PIL import Image
#Se crea una lista vacia
images = []
#Se genera un bucle for de modo que arg recorre sys.arg[] desde la posicion uno a la final
for arg in sys.argv[1:]:
    #Se abre el archivo de imagen que se ingresa por linea de comando
    image = Image.open(arg)
    #Se añade a la lista
    images.append(image)
#Se guarda la imagen, se guardan todos los fotogramas a añadir, se añaden los nuevos fotogramas
#se establece una duracion y se indica si se desea un loop infinito
images[0].save(
    "costumes.gif", save_all=True, append_images = [images[1]], duration = 200, loop=0
)

#NOTA: LAS IMAGENES SE TRADUCEN EN NUMEROS BINARIOS Y ESO ES LO QUE SE TRASPASA A LA LISTA
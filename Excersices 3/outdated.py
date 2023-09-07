"""
Implementar un programa que pida una fecha en formato MM/DD/YY o MM DD, YY e imprimir dicha fecha en
formato YY/MM/DD
"""
#diccionario con meses del año
dicMM ={"January":1,
         "Frebuary":2,
         "March":3,
         "April":4,
         "May":5,
         "June":6,
         "July":7,
         "August":8,
         "September":9,
         "October":10,
         "November":11,
         "December":12
    }
while True:
    try:
        #Fecha por teclado
        fecha = input("Date: ")
        #Quitar espacios laterales y frontales y añadir mayuscula al inicio de cada letra
        fecha = fecha.title().strip(" ")
        #Diccionario que incluye caracteres especiales a considerar dentro de las fechas
        separadores = {" ":"/",",":""}
        #Aplicar diccionario a STR para obtener la siguiente forma str/str/str
        trans = fecha.maketrans(separadores)
        fecha = fecha.translate(trans)
        #Separar en MM, DD, YY
        MM, DD, YY = fecha.split("/")
        #Año y dia a numero entero
        DD = int(DD)
        YY = int(YY)
        #Si MM es alfabetico entonces MM toma valor de su numero entero correspondiente al diccionario
        if MM.isalpha()==True:
            MM = dicMM[MM]
        else:
            #De lo contrario MM se vuelve entero
            MM = int(MM)
        #Condicional de mes y dias
        if 1<=MM<=12 and 1<=DD<=31:
            print(f"{YY}-{MM:02}-{DD:02}")
            break
        else:
            pass
    #Excepcion para volver a preguntar sin salir del programa
    except (ValueError,KeyError):
        pass



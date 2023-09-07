# Implementar un programa que realice una lista de compras con n° de cantidad y nombre del articulo

def main():
    list = []
    lista_compras(list)


def lista_compras(list):
    while True:
        try:
            item = input("Add: ")
            #Convierte string en mayuscula y quita los espacios de izquierda y derecha
            item = item.strip(" ").upper()
            #Agrega a la lista nuevos elementos
            list.append(item)
        except EOFError:
            #Ordena de manera alfabetica una lista
            list = sorted(list)
            dic = {}
            for i in list:
                if i in dic:
                    #Continua con la ejecucion del codigo
                    pass
                else:
                    #Actualiza lo que tiene el diccionario y .count() cuenta cuantas veces se repite un elemento en una lista
                    dic.update({i:list.count(i)})
                    print(dic[i], end=" ")
                    print(i, end="\n")
            break

main()
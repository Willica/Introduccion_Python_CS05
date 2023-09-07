# Lectura de teclado
text = input("Input: ")
# diccionario de vocales (Letras en ASCII)
dic = {97:None,65:None,      #Vocal a
       101:None, 69:None,    #Vocal e
       105:None, 73:None,    #Vocal i
       79:None, 111:None,    #Vocal o
       85:None, 117:None     #Vocal u
}
# Imprimir en pantalla usando el metodo translate llamando al diccionario
print(f"Output: {text.translate(dic)}")

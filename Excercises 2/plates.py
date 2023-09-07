# La matricula debe empezar con 2 letras LISTO
# Pueden contener como maximo 6 caracteres y minimo de dos caracteres LISTO
# Los numeros no pueden estar entre las letras y el primero numero no puede ser un 0
# No se permiten espacios, puntos o cualquier otro simbolo LISTO

plate = input("Plate: ")
plate = plate.upper()

if plate[0:2].isalpha()==True and 2<=len(plate)<=6 and plate.isalnum()==True:
    if plate.isalpha() == True:
        print("Vali3do")
    else:
        for caracter in plate:
            if caracter.isnumeric() == True and caracter != "0":
                text = plate.split(caracter)
                if text[1].isnumeric() == True:
                    print("Valido")
                    break
                else:
                    print("Invalido")
                    break
            elif caracter == "0":
                print("Invalido")
                break
else:
    print("Invalido")


# La matricula debe empezar con 2 letras LISTO
# Pueden contener como maximo 6 caracteres y minimo de dos caracteres LISTO
# Los numeros no pueden estar entre las letras y el primero numero no puede ser un 0 LISTO
# No se permiten espacios, puntos o cualquier otro simbolo LISTO

def main():
    plate = input("Plate: ")
    if is_valid(plate) == "Valido":
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if plate[0:2].isalpha()==True and 2<=len(plate)<=6 and plate.isalnum()==True:
        if plate.isalpha() == True:
            return "Valido"
        else:
            for caracter in plate:
                if caracter.isnumeric() == True and caracter != "0":
                    text = plate.split(caracter)
                    if text[1].isnumeric() == True or text[1] == "":
                        return "Valido"
                    else:
                        return "Invalido"
                elif caracter == "0":
                    return "Invalido"
    else:
        return "Invalido"

main()
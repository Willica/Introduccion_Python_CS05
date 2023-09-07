def main():
    hora_formato24h = input("Que hora es? ")
    hora,minutos = hora_formato24h.split(":")
    hora = float(hora)
    minutos = float(minutos)
    print(hora_de(convert(hora,minutos)))

def convert(hora,minutos):
    minutos = minutos/60
    hora_convertida = hora+minutos
    return hora_convertida

def hora_de(time):
    if 7<=time<=8:
        return"Hora del desayuno"
    elif 12<=time<=13:
        return "Hora del almuerzo"
    elif 18<=time<=19:
        return "Hora de la cena"
    else:
        return "Hora de hacer nada"

if __name__ == "__main__":
    main()
    







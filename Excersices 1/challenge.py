def main():
    hora_formato12h = input("Que hora es? ")
    hora_formato12h = hora_formato12h.lower()
    hora,minutos = hora_formato12h.strip(".a.m.p.m.").split(":")
    hora = float(hora)
    minutos = float(minutos)
    print(hora_de(convert(hora,minutos),hora_formato12h))

def convert(hora,minutos):
    minutos = minutos/60
    hora_convertida = hora+minutos
    return hora_convertida

def hora_de(time,tipo):
    if "a.m" in tipo:
        if 7<=time<=8:
            return "Hora del desayuno"
        elif 12<=time:
            return "Hora del almuerzo"
    elif "p.m" in tipo:
        if time==1:
            return "Hora del almuerzo"
        elif 6<=time<=7:
            return "Hora de la cena"

if __name__ == "__main__":
    main()
    
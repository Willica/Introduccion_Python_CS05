def main():
    hora = input("¿Que hora es? ")
    horas,minutos = hora.lower().strip(" ").replace(".","").split(":")
    minutos,tipo = minutos.split(" ")
    horas = float(horas)
    minutos = float(minutos)
    print(hora_de(convert(horas,minutos,tipo)))

def convert(horas,minutos,tipo):
    if tipo == "am":
        minutos = minutos/60
        hora_convertida = horas + minutos
        return hora_convertida
    elif tipo == "pm":
        minutos = minutos/60
        hora_convertida = (horas+12) + minutos
        return hora_convertida
    
def hora_de(time):
    if 7<=time<=8:
        return "Hora del desayuno"
    elif 12<=time<=13:
        return "Hora del almuerzo"
    elif 18<=time<=19:
        return "Hora de la cena"

main()



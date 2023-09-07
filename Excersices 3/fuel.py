# x no puede ser mayor que 4 y menor que 0
# y no puede ser distinto de 4

def main():
    print(f"{percent()}%")

def percent():
    while True:
        try:
            fraccion = input("Fracción: ")
            x, y = fraccion.split("/")
            x = int(x)
            y = int(y)
            porcentaje = int((x/y)*100)
            if 0<=x<=4 and y == 4:
                return porcentaje
        except (ValueError, ZeroDivisionError):
            pass

main()
    


# Funcion principal
def main():
    # Lectura de valores por teclado
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # Calculo de portencaje
    tip = dollars * percent
    # Imprimir en pantalla, considerando solo 2 valores luego de la coma
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Borrar str $ del inicio
    d = d.removeprefix("$")
    # Pasar a flotante
    d = float(d)
    # Devuelve a la variable d
    return d


def percent_to_float(p):
    # Borrar str % del final
    p = p.removesuffix("%")
    # Pasar a flotante
    p = float(p)/100
    # Devuelve la variable p
    return p

# Llamado a función principal
main()
# Funcion
def energy(masa):
    c = 300000000
    E = masa*c**2
    return E

def main():
    m = float(input("Ingrese la masa: "))
    print(energy(m))

main()
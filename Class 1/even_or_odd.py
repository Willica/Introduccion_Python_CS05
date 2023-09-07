# Codigo muy reducido de si un numero es par o no

def main():
    x = int(input("Valor de x: "))
    if is_even(x):
        print("El numero es par")
    else:
        print("El numero es impar")

def is_even(n):
    return n % 2 == 0

main()
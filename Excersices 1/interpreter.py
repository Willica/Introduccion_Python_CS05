def main():
    operacion = input("Introduzca la operacion: ")
    x,y,z = operacion.split(" ")
    x = float(x)
    z = float(z)
    print(round(interpretador(x,y,z),1))

def interpretador(x,y,z):
    if y == "/":
        return x/z
    elif y == "*":
        return x*z
    elif y == "+":
        return x+z
    else:
        return x-z
    
main()
def main():
    numero = input("Cual es la respuesta a la gran pregunta de la vida: ")
    numero = str.lower(numero)
    if PreguntaVida(numero) == True:
        print("Si!")
    else:
        print("No!")

def PreguntaVida(n):
    return True if n == "forty-two" or n == "forty two" or n == "42" else False

main()

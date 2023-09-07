# Diccionario
dic = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
#Bucle infinito
while True:
    try:
        # Lectura de teclado
        item = input("Item: ")
        item = item.strip().title()
        # Imprimir con dos
        print(f"Price: ${dic[item]:.2f}")
    except KeyError:
        ...
    except EOFError:
        break
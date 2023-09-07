# Problema de saludo, si tiene h $20 si empieza con hello $0 si no empiza con h entonces $100
saludo = input("Saludo: ")
saludo = saludo.lower()
#"""
if saludo.startswith("hello") == True:
    print("$0")
elif saludo.startswith("h") == True:
    print("$20")
else:
    print("$100")
#"""
"""   
match saludo:
    case saludo.startswith("hello"):
        print("$0")
    case saludo.startswith("h"):
        print("$20")
    case _:
        print("$100")
"""
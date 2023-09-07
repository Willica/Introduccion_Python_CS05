# Primera parte suma
""""
x = float(input("x = "))
y = float(input("y = "))
z = round(x + y)
print(f"La operacion da como resultado {z:,}")
"""
# Segunda parte division, reducir decimales de la variable flotante
""""
x = float(input("x = "))
y = float(input("y = "))
z = round(x / y,2)
print(z)
"""
# Tercera parte, cortando decimales con print
""""
x = float(input("x = "))
y = float(input("y = "))
z = x / y
print(f"{z:.2f}")
"""
# Cuarta parte
def main():
    x = float(input("x = "))
    print(f"x al cuadrado es {square(x)}")

def square(n):
    return n*n


main()
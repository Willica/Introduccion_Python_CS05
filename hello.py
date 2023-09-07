# Primer programa
""""
def hello(to="World"):
    to = to.strip().title()
    print(f"Oa {to}")

hello()
name = input("Su nombre es: ")
hello(name)
"""
# Segundo programa

def main():
    hello()
    name = input("Su nombre es: ")
    hello(name)

def hello(to="World"):
    to = to.strip().title()
    print(f"Oa {to}")

main()

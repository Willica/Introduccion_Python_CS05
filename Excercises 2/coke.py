# Acepta monedas de $5, $10 y $25 pesos y el valor de la bebida es $50

print("Amount due: $50")
coin = int(input("Insert Coin: $"))

while coin >25:
    print("Amount due: $50")
    coin = int(input("Insert Coin: $"))

while coin <= 25:
    vuelto_incial = 50 - coin
    print(f"Amount due: ${vuelto_incial}")
    coin = int(input("Insert Coin: $"))
    vuelto = vuelto_incial-coin
    while vuelto > 0:
        print(f"Amount due: ${vuelto}")
        coin = int(input("Insert Coin: $"))
        vuelto = vuelto - coin
    print(f"Change Owed: ${abs(vuelto)}")
    break



        

        
        




# Acepta monedas de $5, $10 y $25 pesos y el valor de la bebida es $50

coin = 50

while coin >25:
    print("Amount due: $50")
    coin = int(input("Insert Coin: $"))

while coin <= 25:
    vuelto = 50 - coin
    while vuelto > 0:
        print(f"Amount due: ${vuelto}")
        coin = int(input("Insert Coin: $"))
        vuelto = vuelto - coin
    print(f"Change Owed: ${abs(vuelto)}")
    break
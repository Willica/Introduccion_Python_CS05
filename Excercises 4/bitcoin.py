"""
Implementar un programa llamado bitcoin.py

- Proponer al usuario ingresar en una linea de comando el valor a convertir (sys.argv[]), si dicho valor
no puede ser convertido a flotante entonces se debe arrojar un error via sys.exit[].
- Consulta la API del índice de precios de Bitcoin de CoinDesk en https://api.coindesk.com/v1/bpi/currentprice.json, 
que devuelve un objeto JSON, entre cuyas claves anidadas se encuentra el precio actual de Bitcoin como 
flotante. Asegúrese de detectar cualquier excepción.
- Genera el costo actual de Bitcoins en USD con cuatro decimales, utilizando como separador de miles.
"""
#Importacion de librerias
import requests
import sys
import json
#Intentar
try:
    #Lectura de valor en linea de comando
    value = float(sys.argv[1])
    #Abrir sitio web mediante codigo para obtener infromación
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #Convierte la respuesta obtenida a formato json
    response = response.json()
    #Navegacion a traves de claves diccionario response
    tipos_de_monedas = response["bpi"]
    tipo_de_moneda = tipos_de_monedas["USD"]
    valor_en_moneda = tipo_de_moneda["rate_float"]
    #Calculo valor final
    valor_final = value*valor_en_moneda
    #Imprimir en formato con , y 4 flotantes despues del punto
    print(f"${valor_final:,.4f}")
#Si 
except (ValueError,IndexError):
    sys.exit("Missing command-line argument")

#Sirve para ver de mejor forma el formato
#response = json.dumps(response.json(),indent=2)



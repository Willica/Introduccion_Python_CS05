import csv
from tabulate import tabulate
import sys 
    
primer_nombre = []
segundo_nombre = []
casa = []

try:
    if len(sys.argv) == 3:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last_name, first_name= row["name"].split(", ")
                primer_nombre.append(first_name)
                segundo_nombre.append(last_name)
                house = row["house"]
                casa.append(house)

        with open(sys.argv[2],"w",newline = "") as csvfile:
            fieldnames = ["first_name","last_name","house"]
            writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
            writer.writeheader()
            for i in range(len(primer_nombre)):
                writer.writerow({"first_name":primer_nombre[i],
                                "last_name":primer_nombre[i],
                                "house":casa[i]})
    elif len(sys.argv)> 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv)< 3:
        sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")


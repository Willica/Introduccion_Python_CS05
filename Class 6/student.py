"""
#Version 1

with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} esta en {row[1]}")
"""
"""
# Version 2
        
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} esta en {house}")
"""
"""
############################################################################################################
La mejora que incorpora la version 2 respecto a la version 1, radica en que se almacenan en "name" y "home"
los valores del archivo .csv de modo que resulta mas facil de entender la logica del codigo
############################################################################################################
"""
"""
#Version 3

students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
"""
"""
############################################################################################################
La version 3 tiene como objetivo reorganizar los datos importador del .csv de forma alfabetica
############################################################################################################
"""
"""
# Version 4

students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} esta en {student['house']}")
"""
"""
############################################################################################################
La version 4 genera a partir del .csv una lista de diccionarios.
############################################################################################################
"""
"""
#Version 5    
        
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house":house}
        students.append(student)

for student in students:
    print(f"{student['name']} esta en {student['house']}")
"""
"""
############################################################################################################
La version 5 reduce la cantidad de lineas de codigo referente a la version 4
############################################################################################################
"""
"""
#Version 6
    
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house":house}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students,key=get_name):
    print(f"{student['name']} esta en {student['house']}")
"""
"""
############################################################################################################
La version 6 permite reorganizar los nombres de manera alfabetica mediante un nuevo argumento ingresado
a la funcion sorted
############################################################################################################
"""
"""
#Version 7
        
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house":house}
        students.append(student)

for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']} esta en {student['house']}")
"""
"""
############################################################################################################
La version 7 elimina la funcion generada en la version 6 y se reemplaza por una funcion fantasma mediante 
la funcion lambda
############################################################################################################
"""
"""
#Version 8

import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name":name, "home":home})

for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']} esta en {student['home']}")
"""
"""
############################################################################################################
La version 8 incluye la libreria csv que permite realizar operaciones con los archivos .csv de modo de faci_
litar el trabajo.
############################################################################################################
"""
#Version 9

import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name":row["name"], "home":row["home"]})

for student in sorted(students,key=lambda student: student["name"]):
    print(f"{student['name']} esta en {student['home']}")
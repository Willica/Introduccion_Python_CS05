"""
import csv

name = input("What's your name: ")
home = input("What's your home: ")

with open("students_2.csv","a",newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])
"""
import csv

name = input("What's your name: ")
home = input("What's your home: ")

with open("students_2.csv","a",newline="") as file:
    writer = csv.DictWriter(file,fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})
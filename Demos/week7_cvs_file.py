#Piotr's code to create a csv File
import csv

#lista = []

with open("fold1/fold2/data.csv") as d:
  reader = csv.reader(d,delimiter = ",", quotechar ="'")
  for row in reader:
    print(row)
    #lista.append(row)

#print(lista) 







#Piotr's code on how to store on a csv File 
f = open("fold1/fold2/data.csv", "w")

lista = ["name", "mark", "tel"]

for i in lista:
   f.write(i)
   f.write(",")
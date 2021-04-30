#Piotr's code for creating a File 
file = open("gaga.txt")
#file.write("This is an example\nIt makes no sense\nBecause I ran out of ideas!")
#print(file.readlines()[0])
for i in file.readlines():
  print(f"Line : {i}", end = "")
file.close()

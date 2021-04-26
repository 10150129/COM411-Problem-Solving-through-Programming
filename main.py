#Piotr's code on how to creat a File 
#going to open a File 
#file = open("gaga.txt", "a")

#file.write("\nsdghjkhhjjhgk")

#file.close

#going to create a list of lines 
#lista = file.readlines()

#print(lista)

#for line in lista:
  #print(line, end = "")
#print(file.readline(100), end="")  

#How to access data from File 
name = input("Enter file name")
name += ".txt"

f1 = open("john.txt")
f2 = open("harry.txt")

for i in range(3):
  print(f"\033[92mJohn: {f1.readline()}\033[0m", end="")
  print(f"\033[93mHarry: {f2.readline()}\033[0m", end="")
  #the \033[92m will change john lines green
  #\033[93m will make harry lines yellow

f1, f2.close()




    




































     











#Week6 data structures-Dictionary

#dictionary
#a dictionary is a dynamic, unordered and mutable collection of data
#a key-value pair is used to add an element to the dictionary
#the key are being stored in the memore cause of the hasing algorithm 
#we can't have duplicate keys but they have to be unique
#we initialize a dictionary with curly brackets {}
#keys are imutable but the values can be anything you want
#for a value you can have a string, a float, an integer, a list, a tuple
#you can take an item out of a dictionary by quoting the Key 
#

dict1 = {}

dict2 = {"name":"Piotr", "age": 26, "alergy":["coffee", "hard working"]}

dict2["siblings"] = 2

menu = {1:"start", 2: "Find Planet", 3: "Enter new Planet"}
#print(menu[int(input("Enter 1, 2 or 3: "))])
print(menu[2])


#for x in dict2.values():
#  print(x)

#Piotr's code for Dictionary
#start with an empty phone book 

phonebook = {}

while True:
  name = input("Enter the name: ")
  number = input("Enter the number: ")
  phonebook[name] = number
  if input("Type 'x' to stop") == 'x':
    break 

#print(phonebook)
def calling(n, book = {}):
  print(f"calling {n} with a phone number {book[name]}")

calling("Piotr", phonebook)






















     











<<<<<<< HEAD
#Piotr's code on matplotlib, how to visualize data in matplotlib

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,10.5]
y = [10,15.5,18.2,20,25,36,40, 40.7]

plt.xlabel("Age")
plt.ylabel("Height")

plt.step(x,y)

plt.show()




=======
#Piotr's code to handle a Json File 
import json


def shop():
  with open("items.json") as json_file:
    items = json.load(json_file)
  return items 

def save_items(items = {}):
  json_database = open("items.json", "w")
  json.dump(items, json_database, indent = 4)
  json_database.close()


def view_all(products ={}):
  for i in products:
    print(i)

#view_all(shop())
def basket():
  basket = []
  while True:
    item = input("Enter item (or \"stop\"): ")
    if item == "stop":
      break
    else:
      basket.append(item)
  return basket

def till(basket =[]):
  shoplist = shop()
  total = 0.0
  for item in basket:
    print(shoplist[item])
    total += shoplist[item]
  return total


def run():
  print("Welkome to Pete's shop! Please have a look around and add items you like!")
  view_all(shop())
  chosen_items = basket()
  while True:
    print("Are you ready to pay?")
    if input().lower() == "yes":
      to_pay = till(chosen_items)
      print(f"Please pay £{to_pay:.2f} by cash or card")
      break
    else:
      chosen_items += basket()

run()


>>>>>>> b9f6a018369f26187266530e5380578167f46bb7




    





    




































     











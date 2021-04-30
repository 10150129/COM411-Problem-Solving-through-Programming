

#Piotr's code - how to add to the list


def get_fruits():
  fruits = []
  print("How many fruits would you like to enter?")
  n = int(input())
  for i in range(4):
    print("Type in the next fruit:")
    fruits.append(input())
 
  #Print all items
  print("Your fruits are {}".format(fruits))

  #Print only few items by slicing 
  print(f"Sliced list: {fruits[0:5]}")

  #Print only few items by using negative index
  print(f"Negative index:{fruits[-2:0]}")

get_fruits()
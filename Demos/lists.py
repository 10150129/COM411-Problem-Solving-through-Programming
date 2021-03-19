#Piotr's code - how to create a list using code

#Define an empy list
fruits = []

#Define a list with items
vegetables = ["Carrot", "Peas"]

#Add iems to the list
fruits.append("Apple")
fruits.append("Banana")
fruits.append("Tomatoe")
fruits.append("Banana")
print(fruits)

#Remove an item from a list
fruits.remove("Banana")
print(fruits)   

#Remove item by index
del fruits[1]
print(fruits)

#Insert a value not at the end
fruits.insert(1,"Pineapple")
print(fruits)

#Access single element
print(fruits[0])
#Recap Data Structures Week 6 23/03/21

#lists
#a list is an indexed, mutable data structure in wich you can out some data(ex: names)
# you can initialize a list with square brackets
# with a list we can access individual elements from it
#you can also append your list
#you can access, you can modify your list as you please
#the only downside of the list is that is not very memory efficient
#it's not advisible for longer sequences of data

lista = ["herry", "jerry", "terry"]
#print(lista[0])
lista.append("larry")
#print(lista)

#tupples
#a tupple is an imutable data type, that means, once you create a tuple you can not change it, modify it
#it stores the data, it is read only and can't be modified
#i can access a single element from the tupple but I can't change it
#very good if you don't want your user to modify data

tuplex = ("Piotr", 21)
print(tuplex)

#sets 
#set is a structure that does not keep hold of any ordering 
#a set contains only distinct elements
#we can use set structures to check membership and to figure out what is unique
#a set is a heterogeneous data structure, it can hold different data types together
#a set can hold anything you want
#you can't really index a set
#we can add elements to the set, there is no .append with sets, but you can add new elements with the .add method

set1 = {"green", "blue", 24, 99, 7}
set1.add("red")
print(set1)

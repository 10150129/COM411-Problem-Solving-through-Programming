#Piotr's code for Data Types

print("What is your name?")
#Variable is a container which can store data for us in the memory (string, interger, float, bool)
name = input()
print("What is your age?")
age = int(input())
print("What is your bank balance?")
balance = float(input())

print("Welcome {}. You are said to be {} years old. Your bank balance is {:.2f}".format(name, age, balance))




print("What is your name?")
name=input()
print("How old are you (in years)?")
age= int (input())
print("How tall are you (in meters)?")
height= float (input())
print("How much do you weigh (in kilograms)?")
weight= float  (input())
bmi= float(weight()/height()**2)
print("Name{} you are {} years old and your bmi is {} .")
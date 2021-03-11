#Piotr's code


#Program that displays a menu and allows the user to either see a nice message, calculate areas of rectangle or triangle or displays the times table for a number.

print("Please choose an option from the menu:\n\n1-Nice message\n2-Area of rectangle\n3-Area of triangle\n4-Times table")

option = int(input())

if option == 1:
  print("Today will be a good day!")
elif option == 2:
  print("Enter the length of the rectangle:")
  l = int(input())
  print("Enter the width of the rectangle:")
  w = int(input())
  area = w*l
  print("The area of this rectangle was {}" .format(area))
elif option == 3:
  print("Enter the base of the triangle:")
  b = float(input())
  print("Enter the height of the triangle:")
  h = float(input())
  area = 0.5*b*h
  print("The are of this triangle was {}".format(area))
elif option == 4:
  print("What number would you like to see times table for?")
  n = int(input())
  for i in range(1,11,1):
    print("{}*{} = {}".format(n,i,n*i))
else:
  print("There is no such option. Go to Specsavers!")


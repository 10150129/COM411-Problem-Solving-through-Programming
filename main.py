#Sam code activity 3 in week 8 with matplotlib 

import matplotlib.pyplot as plt

def coordinates():
  print("Please enter an x value:")
  x=int(input())

  print("Please enter a y value")
  y=int(input())
  return(x,y)

def path():
  print("retrieving path...")
  x_values=[]
  y_values=[]
  for count in range(4):
    data=coordinates()
    x_values.append(data[0])
    y_values.append(data[1])
  return[x_values, y_values]

def run():
  values=path()
  plt.plot(values[0], values[1], "r--o")
  plt.show()

run()



































    





    




































     











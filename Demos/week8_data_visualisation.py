#Piotr's code on matplotlib, how to visualize data in matplotlib (which is a library)
#plt.plot

import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [10,15.5,18.2,20,25,36,40]

plt.xlabel("Age")
plt.ylabel("Score")

plt.plot(x,y,"mD")

plt.show()

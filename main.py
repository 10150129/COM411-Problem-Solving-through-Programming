#Code on visual animations with matplotlib week9 animation with matplotlib activity 2

import matplotlib.pyplot as plt 
import matplotlib.animation as animation

fig, ax =plt.sublots()

def animate(frame):
  global ax
  ax.set_xlimit(0,10)
  ax.set_ylim(0,10)
  ax.plot(frame,frame)
  return frame

def run():
  global fig 
  simple_animation=animation.FuncAnimation(fig, animate, frames=10, interval=1000)
  plt.show()

run()  

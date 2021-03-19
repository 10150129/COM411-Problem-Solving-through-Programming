#Sam' s code for a simple list

#Find the way
#Two functions:
#1st fucntion = directions
#list directions: move forward, move backward, turn left, turn right
#return function

def directions():
  directions = ["Move forward","Move backward","Turn left","Turn Right"]
  return directions


#2nd function = run (no parameters)
#shoul call the first function - directions
#display the list

def run():
  print(directions())

run()

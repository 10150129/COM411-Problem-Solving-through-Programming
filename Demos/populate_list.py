#Sam's code on populate lists
#Beep and Bop need to make their way from the maze

def directions():
  directions = ["Move forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  dirs = directions()
  for index in range(len(dirs)):
    print("{}: {}".format(index, dirs[index]))
    index = int(input())
menu()

def run():
  route = []
  print("Working out escape route...")
  for count in range(5):
    route.append(menu())
  print(f"Escape route:{route}")

run()


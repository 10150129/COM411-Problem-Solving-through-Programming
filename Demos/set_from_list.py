#Sam's code for creating a set from a list 

def observed():
  observations = []

  for count in range(7):
    print("Please enter an observation:")
    observations.append(input())
  return observations

def run():
  print("Counting observations...")
  observations = observed()

  #populate the observations items
  observations_set = set()
  for observation in observations:
    data =(observation, observations.count(observation))
    observations_set.add(data)

  #display observations_set 

  for data in observations_set:
    print(f"{data[0]} observed {data[1]} times")

run()


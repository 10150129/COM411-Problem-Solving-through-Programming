#Sam's code on how to sort sets

def observed():
  observations = []

  for count in range(5):
    print("Please enter an observation:")
    observations.append(input())

  return observations 

def remove_observations(observations):
  is_running=True 
  while(is_running):
    print("Do you wish to remove an observation (yes/no)?")
    response = input()
    
    if(response =="yes"):
       print("Please enter the observation you wish to remove")
       observation = input()
       observations.remove(observation)
    else:
      is_running=False 

def run():
  observations = observed()
  remove_observations(observations)
  #populate the set(create an empty set)
  observation_set = set()
  for observation in observations:
    data = (observation, observations.count(observation))
    observation_set.add((data))
  #display the set, what we have
  for data in sorted(observation_set):
    print(f"{data[0]} {data[1]}")

run() 

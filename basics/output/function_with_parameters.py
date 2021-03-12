#Escape by ("Jumping over")
#Escape by ("Running around")
#Escape by ("Going deeper!")

#We cannot escape that way!The boulder is too big!
#We cannot escape that way!The boulder is moving too fast!
#That might just work!Let's go deeper!

#The function with single plan and name is "plan"

def escape_by(plan):
  if(plan == "Jumping over"):
    print("We cannot escape that way!The boulder is too big!")
  elif(plan == "Running around"):
    print("We cannot escape that way!The boulder is moving too fast!")
  elif(plan == "Going deeper!"):
    print("That might just work!Let's go deeper!")
  else:
    print("Not sure about the plan!")

#Call to function 
escape_by("Jumping over")
escape_by("Running around")
escape_by("Going deeper!")
escape_by("Not sure about the plan!")
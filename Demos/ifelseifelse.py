print("What is your name?")
n = input()
# print("Do you have a dog? (types True of False)")
# dog = input()
#bool is boolean data type -only stores True/False
#highlight the line of code and type ctrl/
#ctrl/ it toggles the hashtag in front of the line


if len(n) >= 9: #allow length of exactly 9 and greater 
  print("You have a very looooong name!")
  print("Your name contains {} letters".format(len(n)))
elif len(n)> 6:
  print("Your name is a bit long. Consider a nickname")
elif len(n)< 3:
  print("Your name is veeeery short")   
else:  
  print("Your name is quiet okay")
print("This is the END of the program!")
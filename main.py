#Piotr's Code - Recap (functions, lists, tuples)

#Program that invites a small database in the sense that it can:
#insert new students and their marks
#keep continually adding students
#print out students name and their mark 
#average mark of all students (calculate)
#find the maximum mark among all students 

#all_students = [("Gary", 67), ("Uzma", 82), ("Mihai", 76)]
#print(all_students)

def generate_stds():
  print("Enter students name:")
  name = input()
  print("Enter grade:")
  grade = int(input())
  return name, grade 


#to call the function
#print(generate_stds())
#t = generate_stds()
#print(t)


def all_stds():
  all_students = []
  while True:
    all_students.append(generate_stds())
    print("To stop adding students type 0")
    x = input()
    if x == '0':
       break 
  return all_students 

print(all_stds)

def print_students(lista):
  for std in lista:
    print(f"{std[0]} earned a grade {std[1]}")


#print(print_students(all_stds()))


def avr_mark(bob):
  total = 0
  for std in bob:
    total += std[1]
  return total/len(bob)

print(avr_mark(all_stds()))    











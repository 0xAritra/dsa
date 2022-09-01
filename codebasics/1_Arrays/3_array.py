# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
max = int(input("enter max: "))
l = []
for i in range (1, max, 2):
  l.append(i)
print(l)
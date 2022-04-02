import copy
with open('input.txt') as f:
  numbers = f.readlines()
numbers=numbers[0].split(",")


#changing elemnt in list for countable numbers
for z, every in enumerate(numbers):
    numbers[z]=int(every)


fuel_list=[] #made list which will "remember" all the fuel expenses, for every possible road

for standing in range(0,max(numbers)): #standing is my courent position

  fuel=0 #how much fuel I will use to move crabs to actual position(aka "standing")
  for every in numbers: #numerating by numbers/all the crabs positions
    distance=0#how much fuel I will use to move one crab to actual position(aka "standing")
    actual_cost=1 #actual cost of moving one more number towards "standing"
    if every>standing: #checking if the number is highter or lower than "standing"
        for y in range (standing,every): #counting fuel expenses of moving one crab
            distance+=actual_cost
            actual_cost+=1
    else:
        for y in range (every,standing): #counting fuel expenses of moving one crab
            distance+=actual_cost
            actual_cost+=1
    fuel+=distance
  fuel_list.append(fuel)


solution=min(fuel_list) #the least expensive option will cost "solution"
print(solution)
f.close()

#Code is solution to Advent of code 2021, day 7 part 2
#https://adventofcode.com/2021/day/7 part two adds change:
#Instead, each change of 1 step in horizontal position costs 1 more unit of
#fuel than the last: the first step costs 1, the second step costs 2 ect.
with open('input.txt') as f:
  numbers = f.readlines()
numbers=numbers[0].split(",")


#changing elemnt in list for countable numbers
for z, every in enumerate(numbers):
    numbers[z]=int(every)

#made list which will "remember" all the fuel expenses, for every possible road
fuel_list=[] 

#standing is my courent position
for standing in range(0,max(numbers)): 

  #how much fuel I will use to move crabs to actual position(aka "standing")
  fuel=0 
  
  #numerating by numbers/all the crabs positions
  for every in numbers: 
  
    #how much fuel I will use to move one crab to actual position(aka "standing")
    distance=0
    
    #actual cost of moving one more number towards "standing"
    actual_cost=1
    
    #checking if the number is highter or lower than "standing" and 
    #counting fuel expenses of moving one crab
    if every>standing: 
        for y in range (standing,every): 
            distance+=actual_cost
            actual_cost+=1
    else:
        for y in range (every,standing): 
            distance+=actual_cost
            actual_cost+=1
    fuel+=distance
  fuel_list.append(fuel)

#the least expensive option is the answer
solution=min(fuel_list) 
print(solution)
f.close()

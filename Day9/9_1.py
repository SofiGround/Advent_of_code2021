#The code contain the answer to Advent of code Day 9th part 1 challenge
#More about the challenge https://adventofcode.com/2021/day/9
#Code will check and find the lowest positions on the board of numbers.
#The lowest position means that the number is not surranded by any
#smaller number, the lowest position can't be 9.
#The code than will sum up all the small positions on the board

#The code contain the answer to Advent of code Day 9th part 1 challenge
#More about the challenge https://adventofcode.com/2021/day/9
#Code will check and find the lowest positions on the board of numbers.
#The lowest position means that the number is not surranded by any
#smaller number, the lowest position can't be 9.
#The code than will sum up all the small positions on the board

#changing a string board to int board(coutability of it will be usefull later)
with open('input.txt') as f:
  board = f.readlines()
for x, every in enumerate(board):
  every=every.replace("\n","")
  every=list(every)
  for y, sth in enumerate(every):
    every[y]=int(sth)
  board[x]=every


#score is the list of the small positions of the board
score=[]

for x, o in enumerate(board):
    for y, l in enumerate(board[x]):

    #now is the number that we are "standing on" and "looking around" for the
    #smaller number
    now=board[x][y]

    #directions is the list of the posible up, right,
    #down and left (the positions we are checking if they exist to compare
    #them and find the lowest number)
    directions=[]
    directions.append(now)

    #checking if the position above exists
    if x>0:
      up=board[x-1][y]
      directions.append(up)

    #checking if the position below exists
    if x+1<=len(board)-1:
      down=board[x+1][y]
      directions.append(down)

    #checking if the position to the left form "now" exists
    if y+1<=len(board[x])-1:
      left=board[x][y+1]
      directions.append(left)

    #checking if the position to the right form "now" exists
    if y>0:
      right=board[x][y-1]
      directions.append(right)

    #where, is the smallest number from the directions,
    #used to then find if it is the smallest number in the area
    where=min(directions)

    if where==now:
      score.append(now)

    #directions muat be empty every time the loop starts
    directions.clear()


#sulution is the sum of all the scores plus one, besides nines
solution=0
for every in score:
  if every!=9:
    solution+=1+every


print(solution)
f.close()

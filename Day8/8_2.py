#The code represents answer to Day 6th part to Advent of code challenge.
#The code will decrypt line by line incrypted numbers and
#More about how the numbers are incrypted at:
#https://adventofcode.com/2021/day/8
#The part two twist is to decrypt all the numbers past "|" and add them

with open('input.txt') as f:
  lines= f.readlines()

#This loop will change a text to list of lines to make it easier to work with
for x, every in enumerate(lines):
  every=every.replace("\n","")
  every=every.replace("|"," ")
  every=every.replace("  ","")
  every=every.replace(" ",",")
  lines[x]=every


#Loop will check every line of text, change it to long stings of characters
#representing every number and decrypt it.
for y, z in enumerate(lines):
  single_line_list=z.split(",")

  #For every linie every number is incrypted differently.
  #Seven three, remebering combination will help
  #with decrypting three later.
  #Four will "use" the same leeters as five and some of two, the combination
  #will help with decrypting those numbers later.
  seven=[]
  four=[]

  for x,each in enumerate(single_line_list):

    #Some of numbers are uniqly incripted (we know that from reading challenge
    #description). Those numbers are: 7,4,1 and 8.
    #We are taking care of decrypting them first.
    if len(each)==3:

      seven=list(each)
      single_line_list[x]="7"

    if len(each)==4:

      four=list(each)
      single_line_list[x]="4"

    if len(each)==2:

      single_line_list[x]="1"

    if len(each)==7:

      single_line_list[x]="8"


    #Some of numbers will be incripted with the same number of letters,
    #in this case the number of letters is five.
    if len(each)==5:

      #If the sting is made form the same characters as seven then it's 3.
      for l in seven:

        k = sum(1 if char in seven else 0 for char in each)
        if k==3:
          single_line_list[x]="3"
          each="3"

      #If the sting is made of three of the characters of four then it's 5.
      for l in four:

        k = sum(1 if char in four else 0 for char in each)
        if k==3:
          single_line_list[x]="5"
          each="5"
      #If the sting is made of tow of the characters of four then it's 2.
      for l in four:

        k = sum(1 if char in four else 0 for char in each)
        if k==2:
          single_line_list[x]="2"
          each="2"



    #Some of numbers will be incripted with the same number of letters,
    #in this case the number of letters is six.
    if len(each)==6:

      for l in four:
        #If the sting is made of four of the characters of four then it's 9.
        k = sum(1 if char in four else 0 for char in each)
        if k==4:
          single_line_list[x]="9"
          each="9"

      for l in seven:
        #If the sting is made of three of the characters of seven then it's 0.
        k = sum(1 if char in seven else 0 for char in each)
        if k==3:
          single_line_list[x]="0"
          each="0"

      for l in four:
        #If the sting is made of three of the characters of four then it's 6.
        k = sum(1 if char in four else 0 for char in each)
        if k==3:
          single_line_list[x]="6"
          each="6"

    #Changing list of string lines to numerical lines, line by line.
    lines[y]=single_line_list



#Making chageable list of numbers
for y,z in enumerate(lines):
  lines[y] = list(filter(None, lines[y]))

#We have interest in only numbers after "|", we can observe from challenge
#description that they are always made of four digits.
numbers=[]
for k, w in enumerate(lines):
  lines[k]=w[-4:]
  values = ','.join(str(v) for v in lines[k])
  numbers.append(values)
#solution is the sum of the 4 digit numbers in numbers list
solution=0

for x, each in enumerate(numbers):
  each=each.replace(",","")
  each=int(each)
  numbers[x]=each
  solution+=each


print(solution)
f.close()

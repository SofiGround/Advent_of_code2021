import copy
with open('input.txt') as f:
  numerki = f.readlines()
numerki=numerki[0].split(",")

dlugosc=len(numerki)
for x, every in enumerate(numerki):
  every=int(every)
  numerki[x]=every
#print(max(numerki))
fuel_list=[]

for x in range(0,max(numerki)):
  
  fuel=0
  for every in numerki:
    odleglosc=0
    if every>x:
      dead=1
      for y in range (x,every):
        odleglosc+=dead
        dead+=1
    else:
      dead=1
      for y in range (every,x):
        odleglosc+=dead
        dead+=1
    fuel+=odleglosc
  fuel_list.append(fuel) 


wynik=min(fuel_list)
print(wynik)
f.close()

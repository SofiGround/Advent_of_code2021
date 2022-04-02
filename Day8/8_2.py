with open('input.txt') as f:
  linie = f.readlines()

for x, every in enumerate(linie):
  every=every.replace("\n","")
  every=every.replace("|"," ")

  every=every.replace("  ","")
  every=every.replace(" ",",")

  linie[x]=every


#print(linie)
for y,every in enumerate(linie):
  lista=every.split(",")
  seven=[]
  four=[]
  #print(four)
  #print(lista)
  for x,each in enumerate(lista):
    if len(each)==3:
      seven=list(each)
      lista[x]="7"
      #print(seven)
    if len(each)==4:
      #print("aha")
      four=list(each)
      lista[x]="4"

    if len(each)==2:
      lista[x]="1"
    if len(each)==7:
      lista[x]="8"
    if len(each)==5:
      count=0
      for pomoc in seven:
    
        ile = sum(1 if char in seven else 0 for char in each)
        if ile==3:
          lista[x]="3"
          each="3"
          #print(lista)
          #print(pomoc)
        #ile = 0
        #for char in each:
        #  if char in seven:
        #    ile += 1

        #print(seven, each, ile)
        
      for pomoc in four:
        
        bro = sum(1 if char in four else 0 for char in each)
        if bro==3:
          lista[x]="5"
          each="5"
          #print(lista)
        #print(four, each, bro)
      for pomoc in four:
        
        ile = sum(1 if char in four else 0 for char in each)
        if ile==2:
          lista[x]="2"
          each="2"
      



    if len(each)==6:
      for pomoc in four:
    
        ile = sum(1 if char in four else 0 for char in each)
        if ile==4:
          lista[x]="9"
          each="9"
      for pomoc in seven:
    
        ile = sum(1 if char in seven else 0 for char in each)
        if ile==3:
          lista[x]="0"
          each="0"
      for pomoc in four:
        ile = sum(1 if char in four else 0 for char in each)
        if ile==3:
          lista[x]="6"
          each="6"
    linie[y]=lista
#print(linie)
for y,every in enumerate(linie):
  linie[y] = list(filter(None, linie[y]))
wynik=[]
for k, w in enumerate(linie):
  linie[k]=w[-4:]   
  values = ','.join(str(v) for v in linie[k])
  wynik.append(values)
suma=0
for x, each in enumerate(wynik):
  each=each.replace(",","")   
  each=int(each)
  wynik[x]=each
  suma+=each


print(suma)
f.close()

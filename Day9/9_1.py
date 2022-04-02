with open('test.txt') as f:
  poziom = f.readlines()
for x, every in enumerate(poziom):
  every=every.replace("\n","")
  every=list(every)
  for meh, um in enumerate(every):
    every[meh]=int(um)
  poziom[x]=every
pion=list(zip(*poziom))
wynik=[]
for x in range(0,len(poziom)-1):
  #print("uno")
  for y in range(0,len(poziom[x])-1):
    
    teraz=poziom[x][y]
    while type(teraz)!=float:
      
      up=poziom[x-1][y]
      down=poziom[x+1][y]
      left=poziom[x][y+1]
      right=poziom[x][y-1]
      directions=[teraz,up,down,left,right]
      where=min(directions)
      if where==teraz:
        if type(teraz)==float:
          break
        if type(teraz)!=float:
          
          wynik.append(teraz)
          poziom[x][y]=float(teraz)
          break
        
        
      else:
        poziom[x][y]==where
        continue
      
      #print(teraz)
print(wynik)   

      
      



    




f.close()

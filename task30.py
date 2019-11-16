#krivo poluchilos
spisok=['a','b','c','a','b','d','a']
spisok.sort()
length=len(spisok)-1
i=-1
counter=1
for temp in spisok:
    if i>6:
        break
    i+=1
    if temp == temp[i]:
        counter+=1
    else:
        print('there is: ' +str(counter)+'of '+str(temp))
    


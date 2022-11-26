x = int(input(" "))
y = int(input(" "))
for i in range(1,y+1):
    print(i ,end=' ')
    if i%x==0 :
        print("-")
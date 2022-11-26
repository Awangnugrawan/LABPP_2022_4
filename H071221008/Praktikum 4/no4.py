x=y=0


def robot():
    global x, y, string
    for i in string:
        if i=="R" :
            x=x+1
            print(x,y)
        elif i=="L" :
            x=x-1
            print(x,y)            
        elif i=="U" :
            y=y+1
            print(x,y)
        elif i=="D" :
            y=y-1
            print(x,y)
    
string=input()
print(x,y)
robot()

while True:
    string=input()

    if string.lower()=="end":
        break
    elif string.lower()=="start":
        x=0
        y=0
        print(x,y)
    else:
        robot()
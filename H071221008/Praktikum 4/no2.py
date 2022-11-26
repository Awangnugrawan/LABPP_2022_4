a = int(input())
b = int(input())

if b == 0 and b < a:
    print("-infinity")
elif a == 0 :
    print("-infinity")    
else: 
    def getFPB(a, b):    
        if (b == 0):
            return a
        else:
            return getFPB(b, a % b)

    print(f"FPB ({a}, {b}) = {getFPB(a, b)}")
    getFPB(a, b)
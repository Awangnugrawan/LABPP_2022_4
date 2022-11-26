n = int(input())

if n < 0:
    print("Tidak terdefinisi")
else:   
    def faktorial(n):
        if n == 0:
            return 1
        elif n>0 :
            return n*faktorial(n-1)
    print(faktorial(n))
    faktorial(n)


        
 





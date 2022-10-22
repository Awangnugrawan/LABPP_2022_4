a = int(input("input nilai matriks pertama index 1,1: "))
b = int(input("input nilai matriks pertama index 1,2: "))
c = int(input("input nilai matriks pertama index 2,1: "))
d = int(input("input nilai matriks pertama index 2,2: "))
e = int(input("input nilai matriks kedua index 1,1: "))
f = int(input("input nilai matriks kedua index 1,2: "))
g = int(input("input nilai matriks kedua index 2,1: "))
h = int(input("input nilai matriks kedua index 2,2: "))

x = [
    [a,b],
    [c,d],
]
y = [
    [e,f],
    [g,h],
]
       
p = [
    [(a*e)+(b*g),(a*f)+(b*h)],
    [(c*e)+(d*g),(c*f)+(d*h)],
]

for i in range(2):
    if i == 0:
        print(x[i], "x", y[i], "=", p[i])
    else:
        print(x[i], " ", y[i], " ", p[i])

#(1*1)+(2*1),(1*2)+(2*2)] = 1+2,2+4 = 3,6
#[(3*1)+(4*1),(3*2)+(4*2)] = 3+4,6+8 = 7,14
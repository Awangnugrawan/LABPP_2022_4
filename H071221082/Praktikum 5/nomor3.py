#Program mencari duplikat 2 buah array

a = []

x = input("Input array ke 1: ").split(" ")
y = input("Input array ke 2: ").split(" ")

for i in (x):
    for j in (y):
        if i == j:
            a += i

b = set(a)

if len(b) >= 1:
    print (f"Terdapat {len(b)} buah duplikat yaitu {set(map(int, b))}".replace ("{", "(").replace("}", ")"))

else:
    print("Tidak ada duplikat")
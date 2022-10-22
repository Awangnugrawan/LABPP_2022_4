x = set(map(int, input('Input array ke 1: ').split()))
y = set(map(int, input('Input array ke 2: ').split()))
n = []

for i in x:
    for j in y:
        if i == j:
            n.append(str(i))

if len(n) == 0:
    print('Tidak ada duplikat')
else:
    print(f"Terdapat {len(n)} buah duplikat yaitu ({', '.join(n)})")



a = input("Input Array ke 1: ").split()
b = input("Input Array ke 2: ").split()
set_a = set()
set_b = set()

for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(b)):
    b[i] = int(b[i])
set_a.update(a)
set_b.update(b)

tup_a = tuple(set_a & set_b)

if len(tup_a)==0 :
    print("Tidak ada duplikat")
elif len(tup_a) > 1 :
    print(f'Terdapat {len(tup_a)} buah duplikat yaitu, {tup_a}')
elif len(tup_a)==1 :
    print(f'Terdapat {len(tup_a)} buah duplikat yaitu, {tup_a}'.replace(',',''))
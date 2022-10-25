x = input()+'.txt'
y = int(input())

with open("Tabel.txt", "r") as tabel:
    file_as = tabel.read()
    with open(x, "w") as konten:
        konten.write(file_as)
        for i in range(y):
            a = input().replace(" ", "_")
            if len(a) > 20:
                print('gagal')
                exit()
            else:
                b = input()
                c = input()
                konten.write(f"\n|{a.ljust(31)}|{b.ljust(14)}|{c.ljust(12)}|")
        konten.write('\n+-------------------------------+--------------+------------+')
        print("Berhasil")
                
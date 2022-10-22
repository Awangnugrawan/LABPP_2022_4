ukuran = int(input("Ukuran Matriks : "))
matriks_1 = [[int(input(f"Matriks 1 Baris {baris + 1} dan Kolom {kolom + 1} : ")) for kolom in range(ukuran)] for baris in range(ukuran)]
matriks_2 = [[int(input(f"Matriks 2 Baris {baris + 1} dan Kolom {kolom + 1} : ")) for kolom in range(ukuran)] for baris in range(ukuran)]
matriks_3 = [[0 for kolom in range(ukuran)] for baris in range(ukuran)] 
#Matriks 3
for x in range(ukuran):
    for y in range(ukuran):
        for z in range(ukuran):
         matriks_3[x][y] += matriks_1[x][z] * matriks_2[z][y]
print(f"{matriks_1} X {matriks_2} = {matriks_3}")


  #1 x 1 + 2 x 1 =3   2 x 2 + 2 = 6    3 x 1 + 4 = 7    3 x 4 + 2 = 14
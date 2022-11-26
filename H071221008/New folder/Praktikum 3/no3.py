harga_barang = int(input(''))
nilai_uang = int(input(''))
c = int(nilai_uang - harga_barang) #kembalian

seratus_ribu = 0
limapuluh_ribu = 0
duapuluh_ribu = 0
sepuluh_ribu = 0
lima_ribu = 0
dua_ribu = 0
seribu = 0

if c==0 :
    print("Tidak ada kembalian")
elif c<0:
    print("Uang tidak cukup!!!")

    
else :
    while c>=100000 :
        d = c//100000
        seratus_ribu += d
        c = c%100000

    while c>=50000 :
        d = c//50000
        limapuluh_ribu += d
        c = c%50000
        
    while c>=20000 :
        d = c//20000
        duapuluh_ribu += d
        c = c%20000

    while c>=10000 :
        d =c//10000
        sepuluh_ribu += d
        c = c%10000

    while c>=5000 :
        d =c//5000
        lima_ribu += d
        c = c%5000

    while c>=2000 :
        d =c//2000
        dua_ribu += d
        c = c%2000

    while c>=1000 :
        d = c//1000
        seribu += d
        c = c%1000
        
    print(seratus_ribu, "uang Rp. 100.000")
    print(limapuluh_ribu, "uang Rp. 50.000")
    print(duapuluh_ribu, "uang Rp. 20.000")
    print(sepuluh_ribu, "uang Rp. 10.000")
    print(lima_ribu, "uang Rp. 5.000")
    print(dua_ribu, "uang Rp. 2.000")
    print(seribu, "uang Rp. 1.000")

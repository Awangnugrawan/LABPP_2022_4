import os

targetcopy = input("File yang akan dicopy : ") + ".txt"
hasilcopy = input("Nama file setelah di copy: ") +".txt"
cekfile = os.path.isfile(targetcopy)

if cekfile == True:
    print("Berhasil")

else:
    print("Gagal")
    exit()

nama = hasilcopy

with open(targetcopy, "r") as target:
    with open(nama , "w") as hasil:
        for isi in target:
            hasil.writelines(isi)
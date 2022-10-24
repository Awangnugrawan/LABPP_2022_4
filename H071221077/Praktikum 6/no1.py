x = input("Masukkan nama file: ") + ".txt"
y = input("Masukkan nama file baru (copy): ") + ".txt"

try:
    with open(x, "r") as old:
            file_asli = old.readlines()
            with open(y, "w") as new:
                new.write(file_asli)
                print("Berhasil")
except:
    print("gagal")
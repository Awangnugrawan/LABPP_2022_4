x = input("Masukkan nama file: ") + ".txt"
y = input("Masukkan nama file baru (copy): ") + ".txt"

try:
    with open(x, "r") as old:
        file_asli = old.readlines()
        n = []
        file_asli[-1] += "\n"
        for x in file_asli:
            n.append(len(x))
            with open(y, "w") as new:
                for i in file_asli:
                    new.write(i.rjust(max(n))) 
    print("Berhasil")
except:
    print("Gagal")
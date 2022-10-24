file1 = input()
file2 = input()    

try:
    f = open(f"{file1}.txt")
    c = f.read()
    with open(f"{file2}.txt","w") as new_file:
        new_file.write(c)
    print("Berhasil")
except:
    print('Gagal')


nama_file = input("Masukkan nama file : ") + '.txt'
salinan = input("Masukkan nama file salinan : ") + '.txt'

try: 
    with open(nama_file, "r") as fileasli:
        baca = fileasli.read()
except:
    print('\nGagal')
else:
    with open(salinan, 'w') as copy:
        copy.write(baca)
    print('\nBerhasil')
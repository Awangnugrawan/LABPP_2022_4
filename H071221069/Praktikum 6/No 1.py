nama_file = input("masukan nama file : ") + '.txt'
salinan = input("masuian nama file salinan : ") + '.txt'
try:
    with open(nama_file, 'r'  ) as fileasli:
        baca = fileasli.read()
    with open(salinan, 'w') as copy_1:
        copy_1.write(baca)
        print('berhasil')
except:
    print('gagal')
print('===============================================================')
print('Selamat datang! Untuk memulai, silahkan input data anda!')
print('===============================================================')

nama = input('Input nama: ')
umur = input('Input umur: ')
alamat = input('Input alamat: ')

datadiri = {
    'Nama': nama,
    'Umur': umur,
    'Alamat': alamat
}

while True:
    print('===============================================================')
    print(f'Selamat datang {nama}, silahkan pilih opsi')
    print('===============================================================')
    print('1. Detail anda')
    print('2. Ubah Nama')
    print('3. Ubah Umur')
    print('4. Ubah Alamat')
    print('5. Keluar')
    print('===============================================================')
    opsi = int(input('Input opsi: '))
    print('===============================================================')
    if opsi == 1:
        print('Data anda adalah')
        print('Nama:',datadiri['Nama'])
        print('Umur:',datadiri['Umur'])
        print('Alamat:',datadiri['Alamat'])
    elif opsi == 2:
        nama = input('Silahkan input data nama baru: ')
        datadiri['Nama'] = nama
        print('Data anda sukses diperbaharui')
    elif opsi == 3:
        umur = input('Silahkan input data umur baru: ')
        datadiri['Umur'] = umur
        print('Data anda sukses diperbaharui')
    elif opsi == 4:
        alamat = input('Silahkan input data alamat baru: ')
        datadiri['Alamat'] = alamat
        print('Data anda sukses diperbaharui')
    elif opsi == 5:
        print(f'Selamat tinggal {nama}')
        exit()
    else:
        print('Opsi salah, masukkan ulang opsi yang benar!')
#Program mengubah detail data

print("Selamat datang untuk memulai silahkan input data anda")
nama = input("Input nama: ")
umur = input("Input umur: ")
alamat = input("Input alamat: ")

print("=" * 50)
print(f"Selamat datang {nama} silahkan pilih opsi")
print("=" * 50)
print('''1. Detail Anda
2. Ubah Nama
3. Ubah Umur
4. Ubah Alamat
5. Keluar''')
print("=" * 50)

while True:
    x = input("Input Opsi : ")
    print("=" * 50)
    if x == "1":
        print(f'''Data anda adalah
Nama: {nama}
Umur: {umur}
Alamat: {alamat}''' )
        print("=" * 50)
        print(f"Selamat datang {nama} silahkan pilih opsi")

    if x == "2":
        nama_baru = input("Silahkan Input Nama Baru: ")
        print("Data anda sukses diperbarui")
        print ("=" * 50)
        print(f"Selamat datang {nama_baru} silahkan pilih opsi")
        nama = nama_baru

    if x == "3":
        umur_baru = input("Silahkan Input Umur Baru: ")
        print("Data anda sukses diperbarui")
        umur = umur_baru

    if x == "4":
        alamat_baru = input("Silahkan Input Alamat Baru: ")
        print("Data anda sukses diperbarui")
        alamat = alamat_baru

    if x == "5":
        print(f"Selamat Tinggal {nama}")
        break

    print(f'''{("=" * 50)}
1. Detail Anda
2. Ubah Nama
3. Ubah Umur
4. Ubah Alamat
5. Keluar''')
    print("=" * 50)
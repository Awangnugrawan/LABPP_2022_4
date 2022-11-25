import os
import re

data = {
    "nama": "kosong",
    "email": "kosong",
    "password": "kosong"
}

x = data.get("nama")
y = data.get("email")
z = data.get("password")

while True:
    print("=" * 50)
    print("Selamat Datang Silahkan Pilih Opsi Menu Anda")
    print("""1. Detail Anda
2. Ubah Nama 
3. Jumlah Data pada File 
4. Save Data pada File 
5. Buat Data Baru 
6. Keluar""")
    opsi = int(input("Silahkan Pilih Menu Anda : "))
    print("="*50)

    match opsi:
        case 1:
            if (x and y and z) == "kosong":
                print("Data Saat Ini Kosong")
            else:
                print(f'''Data Anda Adalah
Nama : {x}
Email : {y}
Password : {z}''')
                
        case 2:
            if (x and y and z) == "kosong":
                print("Data Saat Ini Kosong")
            else:
                data["nama"] = input("Silahkan Input Nama Baru : ")
                x = data.get("nama")

        case 3:
            file = input("Silahkan Masukkan Nama File : ") + ".txt"
            target = os.path.isfile(file)
            if target == True:
                open_file = open(file, "r")
                read_data = open_file.read()
                banyak_data = read_data.lower().count("nama")
                print(f'''Berhasil
Jumlah Data Pada File : {banyak_data} Data''')
            else:
                print(f"Tidak Terdapat File dengan Nama {file}")
                print("Jumlah Data Pada File: 0 Data")

        case 4:
            if (x and y and z) == "kosong":
                print("Data Saat Ini Kosong")
            else:
                file = input("Silahkan masukkan nama file : ") + ".txt"
                target = os.path.isfile(file)
                if target == False:
                    with open(file, "w") as target:
                        target.write("+" + "=" * 50)
                        target.write("\n|Data yang tersimpan")
                        target.write("\n+" + "=" * 50)
                        target.write("\n|Nama" + " " *12 + ": " + x)
                        target.write("\n|Email" + " " *11 + ": " + y)
                        target.write("\n|Password" + " " *8 + ": " + z)
                        target.write("\n+" + "=" * 50)
                        data["nama"] = "kosong"
                        data["email"] = "kosong"
                        data["password"] = "kosong"

                else:
                    with open(file, "a") as target:
                        target.write("\n|Nama" + " " *12 + ": " + x)
                        target.write("\n|Email" + " " *11 + ": " + y)
                        target.write("\n|Password" + " " *8 + ": " + z)
                        target.write("\n+" + "=" * 50)
                        data["nama"] = "kosong"
                        data["email"] = "kosong"
                        data["password"] = "kosong"
                x = data.get("nama")
                y = data.get("email")
                z = data.get("password")
                
        case 5:
            Nama = input("Silahkan Masukkan Nama Anda : ")
            data["nama"] = Nama
            x = data.get("nama")
            while True:
                Email = input("Silahkan Masukkan Email Anda : ")
                polaEmail = r"[a-z0-9]{1,30}@student\.unhas\.ac\.id"
                a = re.fullmatch(polaEmail, Email)
                if not a:
                    print("=" * 50)
                    print("Email yang Anda Masukkan Salah")
                    print("=" * 50)
                else:
                    data["email"] = Email
                    y = data.get("email")
                    break
            while True:
                Password = input("Silahkan Masukkan Password Anda : ")
                polaPassword1 = r"[\w\s/*-=+)(*&^%$#@!><,.?~`]{8,20}"
                polaPassword2 = r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)"
                b = re.fullmatch(polaPassword1, Password)
                c = re.findall(polaPassword2, Password)
                if not b:
                    print("=" * 50)
                    print("Password harus memiliki panjang 8-20 karakter")
                    print("=" * 50)
                elif not c:
                    print("=" * 50)
                    print("Password yang Andaw Masukkan Terlalu Lemah, Gunakan Minimal 1 Huruf Kapital, Huruf Kecil, dan Angka")
                    print("=" * 50)
                elif (b and c):
                    data["password"] = Password
                    z = data.get("password")
                    break

        case 6:
            print("Sampai Jumpa Lagi")
            print("=" * 50)
            break
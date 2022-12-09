# namaHewan1 = "anjing" 
# jumlahHenwan1 = 4
# namaHewan2 = "burung"
# jumlahHewan = 2
# print(namaHewan)

class Burung:
    def __init__ (self, inputJenis, inputWarna):
        self.jenis = inputJenis
        self.warna = inputWarna
        print("objek Berhasil Dibuat")       
        
    # def say_hello():
    #     print("Halo World")   # pembuatan Blueprint/Template

beo = Burung("Beo", "Hijau")   # objek penggunaan Blueprint/Template

print(beo.__dict__)
print(beo.jenis)
print(beo.warna)

#beo.jenis = inputjenis
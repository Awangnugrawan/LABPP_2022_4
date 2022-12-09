from abc import ABC, abstractmethod  # ketentuan(abstarctbaseclass)

#class parent
class Wisata(ABC):
    #abstract
    @abstractmethod
    def oleholeh(self):
        pass
    
    #consctructor
    def __init__(self, nama, harga):
        self.nama = nama
        self.__harga = harga    #__harga = encapsulation

    #method ubah encapsulation
    def setHarga(self, harga):
        self.__harga = int(harga)   
    
    #method ubah encapsulation
    def getHarga(self):
        return self.__harga

#class Child
class Bali(Wisata):  
    # constructor
    def __init__(self, nama, harga):
        super().__init__(nama, harga)       #super. = inheritance
        self.harga = harga
        self.biaya = 10

    #method biasa
    def setHarga(self, harga):
        self.harga = int(harga)     

    #method polymorphism untuk interface
    def place(self):
        print('Total uang yang digunakan ialah', self.biaya, 'juta rupiah')

    #method abstract class
    def oleholeh(self):
        print('Oleh-oleh yang bisa dibawa pulang dari Bali ialah Joger')

#Class Child
class Lombok(Wisata):   
    #constructor
    def __init__(self, nama, harga):
        super().__init__(nama, harga)
        self.harga = harga
        self.biaya = 5

    #method biasa
    def setHarga(self, harga):
        self.harga = int(harga)

    #method polymorphism untuk interface
    def place(self):
        print('Total uang yang digunakan ialah', self.biaya, 'juta rupiah')

    #method abstract class
    def oleholeh(self):
        print('Oleh-oleh yang bisa dibawa pulang dari Lombok ialah Madu Sumbawa')

#interface
def test_harga(wisata):     
    wisata.place()

#bali variable untuk class Bali
bali = Bali('Circus Waterpark Kuta Bali', 100)
#lombok variable untuk class Lombok
lombok = Lombok('Pink Beach Lombok', 50)

print('BALI')
print(bali.nama + ' adalah tempat wisata di Bali')
print(f'Dengan harga masuk {bali.harga} ribu rupiah')
# memanggil abstrak method
bali.oleholeh()
# memanggil interface
test_harga(bali)

print('\nLOMBOK')
print(lombok.nama + ' adalah tempat wisata di Lombok')
print(f'Dengan harga masuk {lombok.harga} ribu rupiah')
# memanggil abstrak method
lombok.oleholeh()
# memanggil interface
test_harga(lombok)
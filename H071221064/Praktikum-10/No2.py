from abc import ABC, abstractmethod

#class parent
class Motor(ABC):
    #abstrak method
    @abstractmethod
    def helm(self):
        pass

    def __init__(self, produk, mesin):
        self.produk = produk
        self.__mesin = mesin #__mesin itu encapsulation

    #metod ubah encapsulation
    def setMesin(self, mesin):
        self.__mesin = int(mesin)
    
    #metod ubah encapsulation
    def getMesin(self):
        return self.__mesin

#class child
class Yamaha(Motor):
    def __init__(self, produk, mesin):
        super().__init__(produk, mesin) #super. itu inherance
        self.kecepatan = 105
        self.__harga = 'Seribu' #__harga itu encapsulation

    #method biasa
    def setKecepatan(self, kecepatan):
        self.kecepatan = int(kecepatan)

    #method biasa
    def getKecepatan(self):
        return self.kecepatan

    #method ubah encapsulation
    def setHarga(self, harga):
        self.__harga = harga

    #method ubah encapsulation
    def getHarga(self):
        return self.__harga
    
    #method polymorphism untuk interface
    def melaju(self):
        print('Dapat melaju hingga',self.kecepatan,'km/jam')

    #method untuk abstract class
    def helm(self):
        print('Beli Motor Yamaha gratis Helm')

#class child
class Honda(Motor):
    def __init__(self, produk, mesin):
        super().__init__(produk, mesin) #super. itu inherance
        self.kecepatan = 95
        self.__harga = 'Seribu dua' #__harga itu encapsulation
     
    #method biasa
    def setKecepatan(self, kecepatan):
        self.kecepatan = int(kecepatan)

    #method biasa
    def getKecepatan(self):
        return self.kecepatan

    #method ubah encapsulation
    def setHarga(self, harga):
        self.__harga = harga

    #method ubah encapsulation
    def getHarga(self):
        return self.__harga
    
    #method polymophisme untuk interface
    def melaju(self):
        print('Dapat melaju hingga',self.kecepatan,'km/jam')

    #method abstract class
    def helm(self):
        print('Beli Helm gratis Motor Honda')

#interface
def test_kecepatan(motor):
    motor.melaju()

yamaha = Yamaha('Odong-odong', 120)
honda = Honda('Bentor', 120)

print('YAMAHA')
print(yamaha.produk + ' Keluaran terbaru dari Yamaha')
print('Harga Yamaha '+ yamaha.getHarga() )
print(f'Dengan mesin {yamaha.getMesin()} cc')
#memanggil abstrak method
yamaha.helm()
#memanggil interface
test_kecepatan(yamaha)
yamaha.setKecepatan(110)
print(f'kecepatan {yamaha.getKecepatan()} km/jam mencapai limit')

print('\nHONDA')
print(honda.produk + ' Sedikit modifikasi dari Honda')
print('Harga Honda '+ honda.getHarga())
print(f'Dengan mesin {honda.getMesin()} cc')
#memanggil abstrak method
honda.helm()
#memanggil interface
test_kecepatan(honda)



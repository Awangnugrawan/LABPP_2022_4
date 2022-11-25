from abc import ABC, abstractmethod
# polymorphism = parent class punya fungsi sama dgn child class tapi beda isinya.
# Buatlah sebuah class yang menerapkan konsep encapsulation, class abstract, inheritance, dan polymorphism

#Abstract Class
class Hewan(ABC):
    @abstractmethod
    def ukuran(self):
        pass

#Class Parent
class Ikan(Hewan):
    def __init__ (self, nama, habitat_air):
        self.__nama = nama 
        #Encapsulation
        self.__habitat_air = habitat_air 
        #Encapsulation

    #method Ikan
    def ukuran(self):
        print (f"Ikan Pada Umumnya Mempunyai Ukuran Kecil")

#Class Child
class Hiu(Ikan): #Inheritance (Hiu Inheritance dari Ikan)
    def __init__(self, nama, habitat_air):
        super().__init__(nama, habitat_air)
        self._sisik = "Placoid" 
        #Encapsulation
        self._bernafas = "Insang"
        #Encapsulation
        self._rahang = "Sangat Kuat"
        #Encapsulation

    #method Hiu
    def ukuran(self):
        print("Ikan Hiu Termasuk Jenis Ikan Yang Mempunyai Ukuran Besar")

    #method Hiu
    def sisik(self):
        print(f"Sisik Ikan Hiu Berjenis {self._sisik}")

    #method Hiu
    def insang(self):
        print(f"Ikan Hiu Memiliki {self._bernafas}")

    #method Hiu
    def rahang(self):
        print(f"Rahang Ikan Hiu {self._rahang}")

class Mujair(Ikan):
    def __init__(self, nama, habitat_air):
        super().__init__(nama, habitat_air)
        self._sisik = "Stenoid" 
        #Encapsulation
        self._bernafas = "Insang"
        #Encapsulation
        self._rahang = "Sangat Lemah"
        #Encapsulation

    #method Mujair
    def ukuran(self):
        print("Ikan Mujair Termasuk Jenis Ikan Yang Mempunyai Ukuran Kecil")

    #method Mujair
    def sisik(self):
        print(f"Sisik Mujair Hiu Berjenis {self._sisik}")

    #method Mujair
    def insang(self):
        print(f"Ikan Mujair Memiliki {self._bernafas}")

    #method Mujair
    def rahang(self):
        print(f"Rahang Ikan Mujair {self._rahang}")
        
#interface
def tes_ukuran(ikan):
    ikan.ukuran()

#objek
# ikan = "Lele"
objek = Ikan("Ikan", True)
objek1 = Hiu("Hiu", True) 
objek2 = Mujair("Mujair",True)

#panggil interface pada kedua objek
tes_ukuran(objek) #Polymorphism 
tes_ukuran(objek1) #Polymorphism 
tes_ukuran(objek2) #Polymorphism
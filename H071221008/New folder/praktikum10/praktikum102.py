from abc import ABC, abstractclassmethod
# Polymorphism = parent class punya fungsi sama dengan child class tapi beda isinya.
# Encapsulation = membatasi akses atribut
# Inheritance = warisan
# Abstract = cetak biru dari class

#Abstract Class
class Tanaman(ABC):
    def mengeluarkan_bau(self):
        pass

#class parent
class Bunga(Tanaman):                            
    def __init__(self, jenis, beracun):
        self._jenis= jenis  #encapsulation
        self._beracun= beracun #encapsulation

    # method bunga
    def getjenis(self):
        return self._jenis
    # method bunga
    def setjenis(self, jenis):
        self._jenis= jenis
    # method bunga
    def mengeluarkan_bau(self):
        pass

#class child
class Rafflesia(Bunga):                 #inheritance (Rafflesia inheritance dari bunga)
    def __init__(self, jenis, beracun):
        super().__init__(jenis, beracun)
    # method Raflessia
    def mengeluarkan_bau(self):
        print('bunga rafflesia mengeluarkan bau tidak sedap')

class Melati(Bunga):                     #inheritancde
    def __init__(self, jenis, beracun):
        super().__init__(jenis, beracun)
    # method melati
    def mengeluarkan_bau(self):
        print('bunga melati mengeluarkan bau harum')

#interface
def tes_mengeluarkan_bau(bunga):  #polymorphism
    bunga.mengeluarkan_bau()

#object
a = Rafflesia("rafflesia", True)
b = Melati("melati", False)

#pemanggilan interface pd kedua object
a.mengeluarkan_bau()   #polymorphism
b.mengeluarkan_bau()   #polymorphism

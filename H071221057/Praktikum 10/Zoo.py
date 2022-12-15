from abc import ABC, abstractmethod 






#class abstract
#3.abstract adalah digunakan untuk memaksa anakan atau turunannya ada fungsi didalamnya.
#4.penggunaan abstract di kodeku itu ada pada self suara yg se buat untuk semua animal atau hewanku.
class Animal(ABC):
    @abstractmethod
    def suara(self):
        pass
#polymorphism
    def __init__(self, nama):
        self.nama = nama

#Inharitance Hewan(Animal)
#5.Inheritance adalah pewarisan dari kelas parent ke child
#6.penggunaan inheritance di kodeku itu ada pada class animal terus turun ke hewan lalu turun ke kucing dan anjing.
class Hewan(Animal):
    def __init__(self, nama):
        super().__init__(nama)
        #Encapsulation (_)
        self._suara = "Suara"
    
    #Polymorphism
    #7.polymorphism adalah menggunakan interface publik pada setiap hewanku.
#8.penggunaan polymorphism di kodeku itu adalah pada kucing dan anjing bertarung menggunakan.
    def serang(self,target):
        #Encapsulation (_)
        target._health -= self._power
    #Polymorphism
    def bergerak(self):
        print("Bergerak dengan cara")
    #Polymorphism
    def bertarung(self):
        print("Bertarung dengan")
   
#Inharitance
class Kucing(Hewan):
    def __init__(self, nama):
        super().__init__(nama)
        #Encapsulation (_)
        self._health = 200
        #Encapsulation (_)
        self._power = 100
    #Polymorphism
    def cekDarah(self):
        #Encapsulation (_)
        print(self._health)
    #Polymorphism
    def serang(self,target):
        #Encapsulation (_)
        target._health -= self._power
    #Polymorphism
    def bergerak(self):
        print("Kucing bergerak dengan menggunakan kaki dan tangannya")
    #Polymorphism
    def bertarung(self):
        print("Kucing bertarung dengan mengunakan cakarnya")
    #Polymorphism
    def suara(self):
        print("Meow")
#Inharitance    
class Anjing(Hewan):
    def __init__(self, nama):
        super().__init__(nama)
        #Encapsulation (_)
        #1.encapsulation adalah untuk menunjukkan atribut private
#2.penggunaan encapsulation di kodeku itu adalah untuk membuat atribut” tersendiri atau private kepada animal atau hewanku.
        self._health = 250
        #Encapsulation (_)
        self._power = 50
    #Polymorphism
    def cekDarah(self):
        #Encapsulation (_)
        print(self._health)    
    #Polymorphism
    def serang(self,target):
        #Encapsulation (_)
        target._health -= self._power
    #Polymorphism
    def bergerak(self):
        print("Anjing bergerak dengan menggunakan kaki dan tangannya")
    #Polymorphism
    def bertarung(self):
        print("Anjing bertarung menggunakan taringnya")
    #Polymorphism
    def suara(self):
        print("Guk-guk")
       
        
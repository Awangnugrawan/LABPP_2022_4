from abc import ABC, abstractmethod

class Human(ABC):

    @abstractmethod
    def makan(self):
        print("Manusia itu sudah makan")

class Hero(Human):

    def makan(self):
        print("Manusia itu sudah makan")
        

person = Hero()
person.makan()



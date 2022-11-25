from abc import ABC, abstractmethod

class Human(ABC):
    @abstractmethod
    def slogan(self):
        pass

    def __init__(self,name):
        self.name = name

class Hero(Human):
    def __init__(self, name):
        super().__init__(name)
        self._health = 500
        self._power = 50
        self._armor = 8

    def slogan(self):
        print('Hero tidak pernah takut akan kejahatan')

    def attack(self, target):
        target._health -= self._power

    def cekStatus(self):
        print("Health = ", self._health)
        print("Armor = ", self._armor)

    def heal(self):
        self._health += 100

class Paperboy(Hero):
    def __init__(self, name):
        super().__init__(name)
        self._health = 650
        self._armor = 20

    def slogan(self):
        print('Hero tidak pernah takut akan kejahatan')

    def powerup(self):
        self._health += 150
        self._armor -= 10
    
    def ultimate(self, target):
        target.armor -= 5

class Kingshark(Hero):
    def __init__(self, name):
        super().__init__(name)
        self._health = 300
        self._power = 100
        self.penetration = 2

    def slogan(self):
        print('Hero tidak pernah takut akan kejahatan')
    
    def attack(self, target):
        target._health -= self._power
        target._armor -= self.penetration
    
    def powerup(self):
        self._power = 150
        
    def ultimate(self,target):
        target.health -= 200

class Queenrafa(Hero):
    def __init__(self, name):
        super().__init__(name)
        self._healing = 300
        self._power = 0
        self._penetration = 0

    def slogan(self):
        print('Hero tidak pernah takut akan kejahatan')

    def powerup(self):
        self._healing = 500
    
    def ultimate(self, target):
        target._health += self._healing

class Vilain(Human):
    def __init__(self, name):
        super().__init__(name)
        self._health = 350
        self._power = 75
        self._armor = 10
        self._penetration = 3

    def slogan(self):
        print("Tidak ada sesuatu yang indah di dunia ini kecuali kehancuran")

    def attack(self, target):
        target._health -= self._power

    def cekStatus(self):
        print("Health = ", self._health)
        print("Armor = ", self._armor)        

    def buff(self):
        self.power += 10

class Megazone(Vilain):
    def __init__(self, name):
        super().__init__(name)
        self._health = 550
        self._power = 40
        self._armor = 15
        self._penetration = 0

    def slogan(self):
        print("Tidak ada sesuatu yang indah di dunia ini kecuali kehancuran")

    def powerup(self):
        self._health = 700
        self._power = 20
        self._armor = 20

    def ultimate(self, target):
        target._power -= 10

class Scorpio(Vilain):
    def __init__(self, name):
        super().__init__(name)
        self._power = 150
        self._penetration = 5

    def slogan(self):
        print("Tidak ada sesuatu yang indah di dunia ini kecuali kehancuran")

    def powerup(self):
        self._power = 175
        self._penetration = 3

    def ultimate(self, target):
        target._health -= 250
        target._armor -= 7
    
class Viper(Human):
    def __init__(self, name):
        super().__init__(name)
        self._health = 250
        self._armor = 5
        self._power = 0
        self._penetration = 0

    def slogan(self):
        print("Tidak ada sesuatu yang indah di dunia ini kecuali kehancuran")

    def powerup(self):
        self._health = 300
        self._power = 20

    def ultimate(self, target):
        target._penetration -= 1
        target._power -= 25

class Human:
    def __init__(self, name, position):
        self.name = name
        self.__position = position
        self.speed = 1

    # def movement(self, movement):
    #     if movement == "L":
    #         self.__position -= self.speed
    #     elif movement == "R":
    #         self.__position += self.speed

    # def setPosition(self, newPosition):
    #     return self.__position

    # def getPostition(self):
    #     self.__position = newPosition

class Hero(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 15        
        self._health = 0
        self._armor = 15
        self._speed = 3

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, newSpeed):
        self._speed = newSpeed

    def attack(self, target):
        target.setHealth(target.getHealth() - self._power)

    def getPower(self):
        return self._power
    
    def setPower(self, newPower):
        self._power = newPower

    def getHealth(self):
        return self._health

    def setHealth(self, newHealth):
        self._health = newHealth

    def getArmor(self):
        return self._armor

    def setArmor(self, newArmor):
        self._armor = newArmor
    
    def setSpeed(self, newSpeed):
        self._speed = newSpeed

    def getSpeed(self):
        return self._speed

class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._armor = 45
        self._power = 32

    def special(self, target):
        self._power = 26
        self._armor = 30
        self.attack(target)

class Assasin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 35
        self.speed = 4

    def special(self, target):
        self._power = 42
        self.speed = 7
        self.attack(target)

class Support(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._armor = 8
        self.speed = 4

    def special(self, target):
        self.speed = 6
        target.setHealth(target.getHealth() + 150)

warrior = Warrior("Bambang", position=10)
assassin = Assasin("Joko", position=25)
support = Support("Udin", position=30)

health = int(input("Masukkan jumlah darah : "))
print("health (before) ", warrior.getHealth() + health)
assassin.attack(warrior)
print("health (after) ", warrior.getHealth() + health)
print("-"*10)

print("Warrior (health) ", warrior.getHealth() + health)
print("Support (speed) : ", support.getSpeed())

support.special(warrior)

print("Warrior (health) ", warrior.getHealth() + health)
print("Support (speed) : ", support.getSpeed())
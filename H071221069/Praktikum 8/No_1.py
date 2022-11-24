class human:
    def __init__(self, name, age, isMale, tinggi, food):
        self.name = name
        self.age = age
        self.isMale = isMale
        self.tinggi = tinggi
        self.food = food

    def setTinggi(self, tinggi):
        self.tinggi = tinggi
    def getTinggi(self):
        return self . tinggi

    def setAge(self, age):
        self.age = age
    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setGender(self, isMale):
        self.isMale = isMale
    def getGender(self):
        if self.isMale == True:
            return "Male"
        elif self.isMale == False:
            return "Female" 
    def setfood(self, food):
        self.food = food
    def getfood(self):
        return self.food

inputnama = input("Nama = ")
inputumur = int(input("Umur = "))
inputgender = bool(input("Gender = "))
inputfood = input("Food = ")
inputtinggi = int(input("Tinggi = "))

orang = human(inputnama, inputumur, inputgender, inputfood, inputtinggi)

print("\nNama = ", orang.getName())
print("Umur = ", orang.getAge())
print("Gender = ", orang.getGender())
print("Makanan Kesukaan = ", orang.getfood())
print("Tinggi = ", orang.getTinggi())



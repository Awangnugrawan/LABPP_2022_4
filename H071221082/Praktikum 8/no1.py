class Person:
    def __init__ (self, name, age, gender, family):
        self.name = name
        self.age = age
        self.isMale = gender
        self.family = family

    def getName(self):
        return self.name
    def setName(self, nilai):
        self.Name = nilai
        
    def getAge(self):
        return self.age
    def setAge(self, nilai):
        self.age = nilai

    def getisMale (self):
        if inputgender == "True":
            return("Male")
        elif inputgender == "False":
            return("Female")
        else:
            return("Masukkan True atau False")

    def getFamily(self):
        return self.family
    def setFamily(self, nilai):
        self.family = nilai

inputnama = str(input("Nama = "))
inputumur = int(input("Umur = "))
inputgender = str(input("Gender = "))
inputfamily = int(input("Jumlah Anggota Keluarga = "))

orang = Person(inputnama, inputumur, inputgender, inputfamily)

print("\nNama = ", orang.getName())
print("Umur = ", orang.getAge())
print("Gender = ", orang.getisMale())
print("Jumlah Anggota Keluarga = ", orang.getFamily())
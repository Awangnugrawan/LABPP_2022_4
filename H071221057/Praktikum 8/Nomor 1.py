class Person:
    def __init__(self, name, age, isMale, Idola, Asal_Sekolah):
        self.name = name
        self.age = age
        self.isMale = isMale
        self.Idola = Idola
        self.Asal_Sekolah = Asal_Sekolah

    def setAge(self, age):
        self.age = int(age)

    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def setGender(self, isMale):
        self.isMale = isMale
 
    def getGender(self):
        if isMale == True:
            self.isMale = 'male'
            return self.isMale
        elif isMale == False:
            self.isMale = 'female'
            return self.isMale
    
    def setIdola(self, Idola):
        self.Idola = Idola

    def getIdola(self):
        return self.Idola

    def setAsal_Sekolah(self, Asal_Sekolah):
        self.Asal_Sekolah = Asal_Sekolah

    def getAsal_Sekolah(self):
        return self.Asal_Sekolah

name = input('Masukkan nama: ')
age = int(input('Masukkan umur: '))
isMale = input('is Male? True / False: ').upper()
if isMale == 'TRUE':
    isMale == bool(True)
elif isMale == 'FALSE':
    isMale = bool(False)
Idola = input('Masukkan Idola Anda: ')
Asal_Sekolah = input('Sekolah: ')

person = Person(name, age, isMale, Idola, Asal_Sekolah)
print('\nNama saya ' + person.getName())
print(f'Sekarang saya berumur {person.getAge()} tahun')
print(f'Saya berjenis kelamin {person.getGender()}')
print('Idola Saya ' + person.getIdola())
print('Saya berasal dari ' + person.getAsal_Sekolah())


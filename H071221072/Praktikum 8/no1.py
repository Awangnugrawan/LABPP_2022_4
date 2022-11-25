class Data: 
    def __init__(self, nama, umur, gender):
        self.nama = nama
        self.umur = gender
        self.gender = umur 
    def getAge(self,umur ):
        print(umur)
    def getName(self, nama):
        print(nama)
    def getGender(self,gender ):
        if gender == 'male':
            print(gender) 
        else:
            print('False')
nama = input('Masukkan nama: ')
umur = (input('Masukkan umur: '))
gender = input('Masukkan gender: ')
print('1.nama | 2.umur | 3.gender | 4.Semua data')
x = input('data yang ingin di lihat: ')
data_diri = Data(nama, umur, gender)
if x == '1':
    data_diri.getName(nama)
elif x == '2':
    data_diri.getAge(umur)
elif x == '3':
    data_diri.getGender(gender)
elif x == '4':
    data_diri.getAge(umur)
    data_diri.getName(nama)
    data_diri.getGender(gender)
else :
   print('Opsi tidak ada')
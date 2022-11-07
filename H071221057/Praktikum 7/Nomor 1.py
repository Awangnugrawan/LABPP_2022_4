import re

s = input()
#2222222222aaaaaaaaaa2222222322aaaaaaaaaa13c57
#x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779
#spasi = r'\s'
angka1 = r'[24680A-Z,a-z]'
angka2 = r'[13579\s]'
#huruf = r'[A-Z,a-z]'

hasil1 = re.findall(angka2, s[0:40])
#hasil1_spasi = re.findall(spasi, s[0:40])
#hasil2 = re.findall(huruf, s[40:45])
hasil2_angka = re.findall(angka1, s[40:45])
print(len(s))
print(hasil1,hasil2_angka)
if hasil1:
    print('false')
elif hasil2_angka:
    print('false')
elif len(s) == 45:
    print('true')
else:
    print('false')

import re

s = input()
#2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57
#x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779
spasi = r'\s'
angka1 = r'[24680]'
angka2 = r'[13579]'
huruf = r'[A-Z,a-z]'

hasil1 = re.findall(angka2, s[0:40])
hasil1_spasi = re.findall(spasi, s[0:40])
hasil2 = re.findall(huruf, s[40:45])
hasil2_angka = re.findall(angka1, s[40:45])
if hasil1 or hasil1_spasi or hasil2 or hasil2_angka:
    print(hasil1, hasil2, hasil2_angka)
    print('false')
elif len(s) == 45:
    print('true')
else:
    print('false')

# kondisi = r'^[A-Za-z24680]{40}[13579\s]{5}$'

# s = input()
# hasil1 = re.findall(kondisi, s)
# if hasil1:
#     print('true')
# else:
#     print('false')
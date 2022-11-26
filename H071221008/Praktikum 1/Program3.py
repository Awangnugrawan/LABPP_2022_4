jari_jari_alas = int(input('Masukkan Jari-jari : '))
tinggi = int(input('Masukkan Tinggi : '))

r=jari_jari_alas
t=tinggi

import math
# phi = 3.1415926535898
s = (r*r)+(t*t)
S = s**0.5

volume = (math.pi*r*r*t)/3
luas_permukaan = (math.pi*r*S)+math.pi*r*r

print('Volume : ', round(volume,2))
print('Luas Permukaan : ', round(luas_permukaan,2))
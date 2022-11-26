print('\nMenghitung panjang kapal')

h= float(input('\nMasukkan tinggi menara : '))
a = int(input('Sudut elevasi pengamat terhadap ujung belakang kapal : '))
b= int(input('Sudut elevasi pengamat terhadap ujung depan kapal : '))


import math
rad_a= (math.pi/180)*a
tan_a= math.tan(rad_a)

rad_b= (math.pi/180)*b
tan_b= math.tan(rad_b)

ac= tan_a*h
bc= tan_b*h

ab = math.sqrt(math.pow(ac-bc,2))
print ('\nPanjang kapal : ', round(ab,1), 'm')

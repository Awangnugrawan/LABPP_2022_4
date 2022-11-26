from dataclasses import replace


print('\n==============================')
print('   PROGRAM TAGIHAN LISTRIK   ')
print('==============================')

golongan =(input('\nGolongan = '))
daya = float(input('Daya(VA)= '))
pemakaian = float(input('Pemakaian(kWh) = '))
tagihan = pemakaian

if golongan == 'R1' or golongan =='r1':
    if daya == 900 :
        tarif= 1352
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    elif daya==1300 :
        tarif= 1444.70
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    elif daya==2200:
        tarif= 1444.70
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    else : 
        print ('Golongan R1 hanya memiliki daya 900, 1300, dan 2200')
elif golongan == 'R2' or golongan == 'r2':
    if daya >=3500 and daya<=5500 :
        tarif= 1699.53
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    else :
        print ('Golongan R2 hanya memiliki daya 3500-5500')
elif golongan == 'R3' or golongan == 'r3':
    if daya>=6600 :
        tarif= 1699.53
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    else : 
        print ('Golongan R3 hanya memiliki daya 6600 keatas')
elif golongan == 'B2' or golongan == 'b2':
    if daya>=6600 and daya<=200000:
        tarif= 1444.70
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    else :
        print ('Golongan B2 hanya memiliki daya 6600-200000')
elif golongan == 'B3' or golongan == 'b3':
    if daya>200000:
        tarif= 1114.74
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    else :
        print ('Golongan B3 hanya memiliki daya diatas 200000')
elif golongan == 'I3' or golongan == 'i3':
    if daya>=200000:
        tarif= 1314.12
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    else : 
        print ('Golongan I3 hanya memiliki daya 200000 keatas')
elif golongan == 'P1' or golongan == 'p1':
    if daya>=6600 and daya<=200000:
        tarif= 1523.28
        tagihan = pemakaian*tarif
        tagihan = "Jumlah tagihan anda : {:_}".format(tagihan)
        print (tagihan.replace('.',',').replace('_','.'))
    else :
        print ('Golongan P1 hanya memiliki daya 6600-200000')
else:
    print ('Data tidak valid')
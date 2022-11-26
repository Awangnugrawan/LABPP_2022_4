print('-----------------------')
print('\tProgram')
print('-----------------------')
a,b,c,d,e = input(). split(" ")

if a.lstrip('-').isnumeric() and b.lstrip('-').isnumeric() and c.lstrip('-').isnumeric() and d.lstrip('-').isnumeric() and e.lstrip('-').isnumeric():
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    e=int(e)
    
    berapa_angka_genap=0
    berapa_angka_ganjil=0
    berapa_angka_positif=0
    berapa_angka_negatif=0

    # Bilangan genap
    if a % 2 == 0 :
        berapa_angka_genap+=1
    if b % 2 == 0:
        berapa_angka_genap+=1
    if c % 2 == 0:
        berapa_angka_genap+=1
    if d % 2 == 0:
        berapa_angka_genap+=1
    if e % 2 == 0:
        berapa_angka_genap+=1

    # Bilangan ganjil

    if a % 2 == 1 :
        berapa_angka_ganjil+=1
    if b % 2 == 1:
        berapa_angka_ganjil+=1
    if c % 2 == 1:
        berapa_angka_ganjil+=1
    if d % 2 == 1:
        berapa_angka_ganjil+=1
    if e % 2 == 1:
        berapa_angka_ganjil+=1


    # Bilangan positif

    if a>0:
        berapa_angka_positif+=1
    if b>0:
        berapa_angka_positif+=1
    if c>0:
        berapa_angka_positif+=1
    if d>0:
        berapa_angka_positif+=1
    if e>0:
        berapa_angka_positif+=1


    # Bilangan negatif

    if a<0:
        berapa_angka_negatif+=1
    if b<0:
        berapa_angka_negatif+=1
    if c<0:
        berapa_angka_negatif+=1
    if d<0:
        berapa_angka_negatif+=1
    if e<0:
        berapa_angka_negatif+=1

    print(berapa_angka_genap, 'Angka genap')
    print(berapa_angka_ganjil, 'Angka ganjil')
    print(berapa_angka_positif, 'Angka positif')
    print(berapa_angka_negatif, 'Angka negatif')

else:
    print('Inputan tidak valid')

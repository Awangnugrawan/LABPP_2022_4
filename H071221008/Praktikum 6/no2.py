try:
    a = input('Masukkan nama file : ') + '.txt'
    b = input('Masukkan nama file salinan : ') + '.txt'
    check_len= 0 
    with open (a, 'r') as fileasli :
        for x in fileasli :
            if len (x)> check_len :
                check_len = len(x)
                
    with open (a, 'r') as fileasli :
        r = 1
        s = len(fileasli.readlines())
       
    with open(a, 'r') as fileasli : 
        copy = open(b, 'w')
        for i in fileasli:
            if r<s :
                new_text = f"{i.rstrip():>{check_len}}\n"
            else :
                new_text = f"{i.rstrip():>{check_len}}"
            copy.write(new_text)
            r+=1
        copy.close()
    print('\nBerhasil')

except:
    print('\nGagal')
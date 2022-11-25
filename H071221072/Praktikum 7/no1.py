import re

#untuk menginput string yang kita ingin ksih masuk
String_s = input('')
print(len(String_s))

#Kondisi awal dan akhir
awal = r'[0?2?4?6?8?]'
akhir = r'[1?3?5?7?9? ?]'

#program mencari 45 string atau mengecek 45 string
result1, result2 = re.findall(akhir, String_s[0:40]) , re.findall(awal, String_s[40:45])
print(result1 , result2)
if result1:
    print('false')
    exit()
elif result2:
    print('false')
    exit()
if len(String_s) == 45:
    print('true')
else:
    print('false')
    exit()
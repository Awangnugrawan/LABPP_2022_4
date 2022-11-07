import re


string_s= input('masukkan String S : ')
print(len(string_s))
regex1 = r'[0?2?4?6?8?_?a-z?A-Z]'
regex2 = r'[1?3?5?7?9?]'

match= re.findall(regex2, string_s[0:40])
match2= re.findall(regex1, string_s[40:45])

print(match, match2)
if match:
    print('false')
    exit()
elif match2:
    print('false')
    exit()


if (len(string_s)) == 45:
    print('true')
else:
    print('false')


    
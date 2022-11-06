import re

s = input()

if len(s) == 45:
    full = r"^[a-zA-Z[02468]{40}[13579\s]{5}"
    syarat2 = r"[13579\s]"
    syarat3 = r"[a-zA-Z[02468]"

    pola = re.findall(full, s)
    pola1 = re.findall(syarat2, s[0:40])
    pola2 = re.findall(syarat3, s[41:45])

    if pola:
        print("True")
    else:
        print("False")

    if pola1 or pola2:
        print(pola1,pola2)

else:
    print("False")
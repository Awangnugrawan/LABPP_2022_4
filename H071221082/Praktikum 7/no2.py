import re

jumlah = int(input())
x = []

for i in range(jumlah):
    nilai = input()
    x.append(nilai)

for j in (x): 
    polaipv4 = r"^((25[0-5]|2[0-4][\d]|[0-1]?[\d][\d]?)\.){3}(25[0-5]|2[0-4][\d]|[0-1]?[\d][\d]?)$"
    polaipv6 = r"(([0-9a-fA-F]{1,4}?\:){7}([0-9a-fA-F]{4}))$"
    ipv4 = re.match(polaipv4, j)
    ipv6 = re.match(polaipv6, j)
    if ipv4:
        print("IPv4")
    elif ipv6:
        print("IPv6")
    else:
        print("Bukan IP Address")
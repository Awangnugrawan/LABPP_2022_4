from War import Paperboy,Kingshark,Queenrafa,Megazone,Scorpio,Viper
paperboy = Paperboy("a")
kingshark = Kingshark("b")
queenrafa = Queenrafa("c")
megazone = Megazone("d")
scorpio = Scorpio("e")
vipar = Viper("f")

#sebelum
print("Status (Before)")
paperboy.cekStatus()
megazone.attack(paperboy)
#sesudah
print("Status (After)")
paperboy.cekStatus()

print("-"*30)

#sebelum
print("Status (Before)")
paperboy.cekStatus()
queenrafa.ultimate(paperboy)
print("Status (After)")
paperboy.cekStatus()

print("-"*30)
print("Status (Before)")
paperboy.cekStatus()
queenrafa.powerup()
queenrafa.ultimate(paperboy)
paperboy.cekStatus()
print("-"*30)
print("--- SLOGAN ---")
print("=== Slogan Hero ===")
paperboy.slogan()
print("=== Slogan Villain ===")
vipar.slogan()

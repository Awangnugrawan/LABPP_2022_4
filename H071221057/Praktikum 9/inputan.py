from no1 import Warrior, Assasin, Support
warrior = Warrior("bambang", pos_x=10)
assassin = Assasin("joko", pos_x=25)
support = Support("udin",pos_x=30)
# sebelum
print("health (before)", warrior.getHealth())
assassin.special(warrior)
# setelah
print("health (after)",  warrior.getHealth())
print("-"*10)
# sebelum
print("Warrior (health)" ,warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)
# setelah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())

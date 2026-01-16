# -*- coding: utf-8 -*-
"""
Generování náhodných čísel
---------------------------
V programech často potřebujeme získat náhodné číslo:
- počítač má vybrat z několika rovnocenných možností
  (třeba náhodné testové otázky, tahy hráče, házení
   kostkou, zamíchání karet)

Potřebujeme knihovnu random 
randint(od,do) - vygeneruje náhodné číslo z intervalu <od,do>
               - od a do musí být celá čísla, mohou být i záporná 
choice(data)   - vybere z dat náhodný prvek
               - data jsou obvykle řetězec nebo seznam
"""


import random


# x=random.randint(1,6)
# print ("Kostka hodila", x)

# pismeno=random.choice("abcdefghijklmnopqrstuvwxyz")
# print("Písmeno:", pismeno)

# pozdrav=random.choice(["ahoj","nazdar","grüs"])
# print("Náhodný pozdrav:", pozdrav)

# kod=""
# pismeno=random.choice("abcdefghijklmnopqrstuvwxyz")
# kod+=pismeno
# pismeno=random.choice("abcdefghijklmnopqrstuvwxyz")
# kod+=pismeno
# pismeno=random.choice("abcdefghijklmnopqrstuvwxyz")
# kod+=pismeno
# print(kod)


# test, zda měsíc má 31 dnů
# mesic = random.randint(1,12)
# print(mesic)
# if mesic in [1,3,5,7,8,10,12]:
#     print("Má 31 dnů.")
# else:    
#     print("Nemá 31 dnů.")


"""
Úkol:
1) Naprogramujte hru KÁMEN, NŮŽKY, PAPÍR.
   Hraje člověk proti počítači.

Vytvořte pomocné proměnné a používejte je místo hodnot:
kamen="k"
nuzky="n"
papir="p"

Náhled programu:
Hrajeme hru kámen, nůžky, papír
(k) Kámen
(n) Nůžky
(p) Papír
Zadej písmeno:
    
vyhodnocení + výpis + ošetření správného vstupu

"""

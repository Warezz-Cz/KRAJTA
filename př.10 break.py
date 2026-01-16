import os
os.system("cls")
import random

"""
cislo = ""
x = 0
while x < 5:
    cislo = float(input("Zadejte číslo: "))
    x +=1
    if cislo < 0:
        break
"""
"""
pokus = 0
x = 0
y = random.randint(1,10)
print("Myslím si číslo")
while x != y:
    x = float(input("Zadejte číslo: "))
    pokus += 1
    if x == y:
        print("Správně")
        break
    elif x > y:
        print("číslo je nižší")
    else:
        print("číslo je větší")
    
print("počet pokusů: ", pokus)
"""

retezec = (input("Zadejte číslo: "))
delka = len(retezec)
i = 0
mez = 0
while i < delka:
    mez += int(retezec[i])
    i += 1
print(mez)
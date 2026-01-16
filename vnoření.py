import os
os.system("cls")
import random
import math
from datetime import date

"""1) Vytvořte cyklus, který vypíše 6x dnešní datum.
   Celý cyklus zopakujte druhým cyklem 8x. """

"""
for x in range(8):
    for y in range(6):
        print(date.today())
"""
"""
2) Napište program, který 5x pod sebou vytiskne vaše 
   jméno (cyklem).
   Celý program zopakujte 30x (cyklem), vždy po 5-ti jménech
   vložte prázdný řádek.
   Napište před každé jméno jeho celkové pořadové číslo.
"""
"""
poradi=0
for y in range(30):
    for x in range(5):
        poradi+=1
        print(poradi, "Fido")
    print('')
"""
"""
3) Načtěte od uživatele počet hráčů a pro každého
   vypište 6 hodů kostkou. Hráčů může být libovolné 
   množství. Ukázka pro 3 hráče.
   1. Hráč: 5 6 1 2 4 3
   2. Hráč: 4 4 1 2 6 3
   3. Hráč: 2 3 5 4 1 2
"""
"""
poradi = 1
hraci = int(input("Zadejte počet hráču: "))
for y in range(hraci):
    hod=[]
    for x in range(6):
        hod+=[random.randint(1,6)]
    print(str(poradi)+". Hráč:",*hod)
    poradi +=1
"""
"""
4) Vytvořte následující výpis pro libovolné n (toto bylo 4):
   1 : 1
   2 : 12 
   3 : 123
   4 : 1234
"""
"""
seznam = []
x = int(input("Zadejte počet: "))
for y in range(1,x+1):
    seznam+=[y]
    print(y,":",str*seznam)
"""

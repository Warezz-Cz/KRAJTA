# -*- coding: utf-8 -*-
"""
                Seznamy
- uvádějí se v [], jednotlivé hodnoty se oddělují čárkou
- mohou obsahovat libovolná data i další seznamy
"""
# a = 10
# b = -5
# sez = [a,b]
# a = 0
# b = 0
# print(sez)


# seznam = []    #prázdný seznam
# print(seznam)    

# seznam = [4, 2, 7]
# print(*seznam)    #print(4, 2, 7)
# print(seznam)     #print([4, 2, 7])

# for prvek in seznam:
#     print(prvek, end=" ")


seznam=[3,"Python",3.0,[1,0,1],False,1000]
# print(seznam)

# print(seznam[1])
# print(seznam[1][1])

# seznam[2]="Programování" #přiřazení
# print(seznam)

    
# seznam=seznam+seznam #spojování seznamů
# print(seznam)

# seznam=[0]*10 #násobení seznamu konstantou
# seznam[5]="Figurka"
# print(seznam)


# import random
# seznam=[]
# for i in range(10):
#     seznam+=[random.randint(0,20)]
# print(seznam)


# seznam=list("Python")
# print(seznam)

# print(range(10,20))
# print(list(range(10,20)))

# print(seznam[:4]) #podseznam [0..3]
# print(seznam[1:4]) #podseznam [1..3]
# print(seznam[1:6:2]) #podseznam [1..5] každý 2. prvek

"""
Úkol:
1) Vytvořte 5-ti prvkový seznam obsahující nuly a 
   vypište jej.
   Pomocí cyklu načtěte 5 nových hodnot z klávesnice a 
   přepište nuly v seznamu těmito novými hodnotami.
   Seznam vypište.
2) Zjistěte, jestli se v seznamu nachází hodnota 20.
   (použijte operátor in)
3) Pomocí cyklu najděte v tomtéž seznamu nejmenší 
   prvek.

Navíc:
4) Vytvořte si seznam 20ti náhodných čísel.
   Načtěte od uživatele hodnotu z klávesnice a zjistěte,
   kolikrát se daná hodnota nachází v seznamu. 
"""


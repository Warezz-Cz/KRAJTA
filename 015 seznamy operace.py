# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 @author: Radek
"""
"""
        Seznamy a jejich operace
append(hodnota)       - přidá hodnotu na konec seznamu
count(hodnota)        - zjistí počet výskytů dané hodnoty
insert(index, hodnota)- vloží hodnotu na pozici v seznamu
pop(index)            - odebere prvek z dané pozice
remove(hodnota)       - smaže první výskyt této hodnoty
sort()                - setřídí seznam podle velikosti vzestupně
sort(reverse = True)  - setřídí seznam podle velikosti sestupně

delka=len(seznam)     - zjištění velikosti seznamu
copy()                - vrátí kopii seznamu (ne referenci)
""" 

seznam=[100,2023,1000,3,1,500,17]
seznam=seznam+[2023]
seznam.append(2023) 
# print (seznam)


# print ("Pocet 2023: ",seznam.count(2023))

# seznam.insert(0,"Vlozeno") #vloží hod. na začátek
# print (seznam)


# Pokud neuvedeme index, odebírá z konce seznamu
# x=seznam.pop(0) #Odebere prvek z pozice 0
# print(x)
# print(seznam)


# seznam.remove(2023) #Odebere první výskyt
# print (seznam)


# seznam.sort()
# print(seznam)


ret=["beta","c","a","alfa"]
ret.sort()
print(ret)
ret=["1000","10","20","100"]
ret.sort()
print(ret)


# print(*ret)
# print("beta","c","a","alfa")

# Co uvidíme na výstupu?
sez1 = [1, 7, 9]
sez2 = sez1
sez2.append(50)
print(sez1)
print(sez2)


# sez1 = [1, 7, 9]
# sez2 = sez1.copy()
# sez1.append(50)
# print(sez1)
# print(sez2)


# sez=[1,2,3]
# a=sez
# b=sez[:]
# print(a)
# print(b)

# print (a is sez)
# print (b is sez)
# print (a == sez)
# print (b == sez)


# print ("Seznam má",len(sez),"prvky.")

"""
Úkol:
1) Napište cyklus, který bude načítat z klávesnice 5 
   čísel a postupně je bude dávat na konec prázdného 
   seznamu. Seznam nakonec vypište.
2) Vygenerujte a vypište seznam 20-ti náhodných čísel 
   od 1 do 10.
3) Předchozí seznam setřiďte a vytvořte k němu seznam 
   druhých mocnin. Oba seznamy vypište.
4) Zjistěte, kolikrát se v mocninách vyskytuje 81.
   Odstraňte všechna čísla 81 ze seznamu mocnin. 
5) Uložte do seznamu 6 náhodných hodů kostkou a zjistěte,
   jestli padla postupka tj. všechny hodnoty od 1 do 6 v
   libovolném pořadí.
6) Do seznamu "karty" vložte seřazené všechny karty. 
   Vytvořte seznam "balicek" a vložte do něj zamíchané 
   všechny karty ze seznamu "karty".
   Help: karty=["♥7","♦7","♣7","♠7", ...]
7) Napište simuaci sportky. Člověk zadá 6 čísel, poté 
   počítač vylosuje také 6 čísel a vypíše, která čísla
   jsme uhádli. Čísla  musí být z intervalu 1-49. Čísla
   se nesmí opakovat.
"""
# sazka = []
# while len(sazka) < 6:
#     cislo = int(input("Vsaď číslo od 1 do 49: "))
#     if cislo > 0 and cislo < 50 and cislo not in sazka:
#         sazka.append(cislo)
#     else:
#         print("Chyba, vsaď znovu!")    
# print(sazka)        

# import random
# los = []
# while len(los) < 6:
#     cislo = random.randint(1,49)
#     if cislo not in los:
#         los.append(cislo)
# print(los)        

# vyhra = []
# for cislo in sazka:
#     if cislo in los:
#         vyhra.append(cislo)

# print("Vaše výherní čísla:", vyhra)        



"""
DU) 
1) Naprogramujte jakoukoli hru s kostkami pro alespoň dva 
   hráče, jeden z nich bude počítač. 
2) Hra musí být dostatečně složitá a pro pro uchování hodů 
   bude používat seznamy. Příliš jednoduché hry budou vráceny
   k přepracování.
3) Musí být zobrazena pravidla.
4) Hra po spuštění zobrazí jednoduché textové menu:
   
   1) Zobraz pravidla
   2) Hrát hru
   3) Nastavení (nepovinná položka)
   4) Konec
   Zadej svou volbu:
       
   Po ukončení hry se program vrací do menu, nedojde k ukončení
   aplikace!
5) Hody hráčů (člověka i počítače) musí proběhnout až po stisku 
   klávesy Enter! 
   Použijte tento příkaz, který v podstatě způsobí čekání programu, 
   dokud uživatel nestiskne Enter: input("Stiskni Enter...").
   Snažte se o přehledné výpisy stavu hry - např. průběžné body
   za kolo a také celkové od začátku hry.
6) Každý musí mít jinou hru! :)   
""" 

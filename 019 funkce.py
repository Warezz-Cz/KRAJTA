# -*- coding: utf-8 -*-
"""
Už známe, protože je používáme.
Existují 2 druhy parametrů - poziční a pojmenované.

Výhody podprogramů:
    1) Přehlednost
    2) Opakované použití - ušetříme psaní
    
Syntaxe:
def Název (parametr1,parametr2,...):
    blok příkazů
    return výsledný výraz

Pozn. Pokud neuvedeme return, vrací se vždy None    

Počet parametrů:
    a) žádné            def Fce()
    b) konkrétní počet  def Fce(x,y,z)
    c) proměnlivý počet def Fce(x,*param)

Implicitní hodnoty parametrů:
    V definici funkce může být do parametru 
    předána implicitní hodnota, která se použije
    v případě, že tento parametr nebude dosazen.
   !Všechny parametry vpravo od něj, musí být také
    implicitní.
"""    

def pozdrav():
    print ("Good morning!")

# pozdrav()


def pozdravy(pocet):
    for i in range(pocet):
        print ("Buenos dias!")

# pozdravy(8)


def super_pozdrav(pocet,text):
    for i in range(pocet):
        print (text)

# super_pozdrav(5,'Guten Tag!')
# super_pozdrav(4,"Wan shang chao")
# super_pozdrav(text='Guten Tag!',pocet=5)



def mocnina1(x):
    vysledek=x**2
    return vysledek

# print(mocnina1(10))


def mocnina2():
    vstup=int(input("Zadej číslo pro umocnění:")) #tohle by zde nemělo být!!! 
    na2=vstup**2
    na3=vstup**3
    
    return (na2, na3)
    print("Ahoj") #toto se ignoruje

# vysledek = mocnina2()
# print(vysledek)



# sez = [6,3,2]
# print(sez.sort())

"""
Úkol:
1) Napište podprogram A_na_X(A,X), která bude mít dva parametry
   A a X a bude počítat a vypisovat hodnotu A na Xtou.
2) Napište podprogram Linear(a,b), která vypíše řešení lineární
   rovnice (ax+b=0). Má dva parametry a,b.     
3) Napište funkci Prumer(a,b,c), která vrátí (return) aritmetický
   průměr ze tří čísel.
4) Napište fci Kostka(), která vrátí hodnotu hodu kostkou.
5) Napište funkci Vrat_Seznam(pocet, od, do), která vrátí
   seznam náh. čísel o daném počtu a rozsahu
6) Vytvořte fci ZasifrujText(txt), která vrátí zašifrovaný
   text tak, že mezi jeho písmena vloží náhodná písmena navíc.
7) Funkce PocetSamohlasek(txt), která vrátí počet samohlásek 
   ze vstupního parametru txt.
8) Funkce Presmycka(txt), která náhodně zamíchá znaky z původního
   textu a vrátí tuto přesmyčku.  
"""














































"""
import random
vstup = input("Zadej slovo: ")
sez = list(vstup)
vystup = ""
while len(sez)>0:
    vystup += sez.pop(random.randint(0,len(sez)-1))

print(vystup)
"""
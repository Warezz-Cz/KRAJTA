import os
os.system("cls")
import math
import random

# 1) Napište podprogram A_na_X(A,X), která bude mít dva parametry
#    A a X a bude počítat a vypisovat hodnotu A na Xtou.

def ax(a,x):
    print(a**x)

# ax(2,64)

# 2) Napište podprogram Linear(a,b), která vypíše řešení lineární
#    rovnice (ax+b=0). Má dva parametry a,b.

def linear(a,b):
    if (a!=0):
        print("rešení rovnice je: ",-b/a)
    else:
        print("rovnice nemá rešení")

# while(True):
#     os.system("cls")
#     a = int(input("Zadejte a: "))
#     b = int(input("Zadejte b: "))

#     linear(a,b)

#     input()
        
# 3) Napište funkci Prumer(a,b,c), která vrátí (return) aritmetický
#    průměr ze tří čísel.
        
def prumer(a,b,c):
    print((a+b+c)/3)

# a = int(input("Zadejte a: "))
# b = int(input("Zadejte b: "))
# c = int(input("Zadejte c: "))

# prumer(a,b,c)
    
# 4) Napište fci Kostka(), která vrátí hodnotu hodu kostkou.
    
def kostka():
    print(random.randint(1,6))

# while(True):
#     os.system("cls")
#     kostka()
#     input()
    
# 5) Napište funkci Vrat_Seznam(pocet, od, do), která vrátí
#    seznam náh. čísel o daném počtu a rozsahu
    
def Vrat_Seznam(pocet, od, do):
    seznam=[]
    for i in range(pocet):
        cislo=random.randint(od, do)
        seznam+=[cislo]
    print(*seznam)


# while(True):
#     os.system("cls")
#     pocet = int(input("Zadejte pocet: "))
#     od = int(input("Zadejte od: "))
#     do = int(input("Zadejte do: "))
#     Vrat_Seznam(pocet,od,do)
#     input()
    
# 6) Vytvořte fci ZasifrujText(txt), která vrátí zašifrovaný
#    text tak, že mezi jeho písmena vloží náhodná písmena navíc.
    
def ZasifrujText(txt):
    abeceda ="QWERTZUIOPASDFGHJKLYXCVBNMqwertzuiopasdfghjklyxcvbnm1234567890"
    text=""
    for i in txt:
        cislo=random.randint(0,57)
        pismeno=i+abeceda[cislo]
        text+=pismeno
    print(text)
    
zadani=input()
ZasifrujText(zadani)
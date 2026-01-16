# -*- coding: utf-8 -*-
"""
Výjimky
- slouží k zachycení chyb a problémových stavů
try:
    blok s kódem, kde může nastat chyba
except:
    blok, který se provede při chybě
else:
    nepovinný blok, který se provede, když nenastane
    chyba    
"""


# cislo=-10
# try:
#     odmocnina=math.sqrt(cislo)
#     print("Odmocnina z",cislo,"je",odmocnina)
# except:
#     print("Chyba, odmocnit lze jen nezáporná čísla!")    


# x=8
# y=0
# try:
#     print ("Pokus o výpočet podílu")
#     vysledek=x/y
#     print (vysledek)
# except:
#     print ("Nastala chyba deleni")
# else:    
#     print ("Deleni probehlo v poradku.")



# import math
# vstup=False
# while (vstup==False):
#     try:
#         cislo=float(input("Zadej kladné číslo:"))
#         odmoc=math.sqrt(cislo)
#         print(odmoc)
#     except:
#         print("Zadávejte pouze kladná čísla!!!")
#     else:    
#         vstup=True

# try:
#     5 + 5
# except TypeError:
#     print ("Chyba s typy")
# except ZeroDivisionError:
#     print ("Nastala chyba deleni nulou")
# except NameError:
#     print ("Chyba jmena ")
# except:
#     print ("Jina vyjimka")
# else:
#     print ("OK")

# try:
#     n = int(input("Zadejte počet dat (1-100): "))
#     if n < 1 or n > 100:
#         raise ValueError("Počet dat musí být od 1 do 100.")
# except ValueError as e:
#     print(f"Chyba: {e}")
#     # exit(1)

# raise - můžeme vyvolat výjimku, třeba když někdo 
#         dosadí špatně parametr funkce, nebo nastane
#         situace, kdy chceme program ukončit s chybou    

# try:
#     x = 10 / 0
# except Exception as e:
#     print(f"Chyba: {e}")


"""
Ukoly:
1) Ošetřete pomocí výjimky převod řetězce na číslo.
2) Spusťte v části try nějakou funkci a dejte jí
   špatný počet parametrů. Vypište vhodnou chybovou hlášku.
3) Vytvořte si seznam o délce 3 a zkuste vypsat 
   4. prvek. Vypište chybovou hlášku.
""" 









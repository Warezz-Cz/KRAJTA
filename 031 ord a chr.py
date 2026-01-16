# -*- coding: utf-8 -*-

"""
Převody znaků
Znakem se rozumí řetězec o délce 1.
ord() - převede znak na jeho ordinální hodnotu (číslo)
chr() - opačná funkce, získáme znak = jednoznakový řetězec
"""


# znak=input('Zadej znak: ')
# cislo=ord(znak)
# print(cislo)


# cislo=int(input('Zadej cislo znaku: '))
# znak=chr(cislo)
# print (znak)

"""
Ukol:
1) Vypište úsek ASCII tabulky od 50 do 100
2) Vypište abecedu z malých písmen do řádku.  
3) Napište funkci NahodnePismeno(), která vrátí 
   náhodné Velké písmeno.
4) Napište funkci PosunSlova(slovo), která vrátí 
   slovo se znaky posunutými o 1. (př: "Ahoj"->"Bipk")
5) Napište funkci NahodneSlovo(), která vygeneruje 
   náhodný řetězec z libovolných malých písmen. Délka 
   bude náhodná mezi 10 a 1.

*) Rozšiřte předchozí funkci tak, aby se střídaly 
   souhlásky a samohlásky. Slovo začíná náhodně 
   samohláskou nebo souhláskou.
   Již nepoužívejte ord() a chr().

"""

for i in range(ord("."),ord("z")+1):
    print(chr(i),end="")
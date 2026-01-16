# -*- coding: utf-8 -*-

"""
Převodní funkce
float() - převede hodnotu na desetinné číslo
10 -> 10.0
"10.154" -> 10.154

int() - převede hodnotu na celé číslo
      - desetinná část je odstraněna 
10.478 -> 10
"12" -> 12
"3.141" -> error! - musím nejprve převést na float: int(float("3.141"))

str() - převede cokoli na  řetězec
400 -> "400"
10.478 -> "10.478"
(10+5j) -> "(10+5j)"

complex() - převede číslo na komplexní
"""

import os
os.system("cls")


# x = input("Zadej číslo: ")
# x = float(x)
# print("Dvojnásobek:", 2 * x)


# y = float(input("Zadej desetinné číslo: "))
# y = int(y)
# print("Převedeno na celé:", y)


# x = 1000
# text = "Vysledek je " + str(x) + "."
# print(text)


"""
Úkol:
1) Načtěte z klávesnice desetinné číslo, 
   vydělte ho 3, převeďte zpět na řetězec 
   a přičtěte k němu jednotku "cm".
   Výsledný řetězec vytiskněte.

2) Načtěte rozměry domu s obdélníkovým 
   půdorysem jako desetinná čísla a spočítejte, 
   kolik m ctverečních polystyrenu potřebujete 
   na zateplení stěn (bez stropu a podlahy,
   okna a dveře se zanedbavaji).   
"""


















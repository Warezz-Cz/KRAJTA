# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 08:35:52 2012

@author: Martin
"""
"""
Materiály:
http://matplotlib.org/
"""    
"""
existuje fce triplot(x,y) - uzavře lomenou čáru
"""

import numpy as np
import matplotlib.pyplot as plt

# x=[0,1,-1,3,4]
# y=[5,2,1,2,-1]
# plt.plot(x,y)
# plt.show() #zobrazení grafu a anulování všech nastavení

# x=np.arange(-5,5,0.1) #vektor x od -5 do 5, krok 0.1
# print(x)

# x=np.linspace(-5,5,30) #vektor x od -5 do 5, 30 hodnot
# print(x)

# y1=2*x+1
# y2=x**2
# y3=x**3

# plt.grid() #zobrazení mřížky - funguje jako přepínač
# # # plt.grid(True) #zobrazení mřížky - nastaví vždy
# plt.title("Graf funkce x3")
# plt.xlabel("Osa x") # popis osy x
# plt.ylabel("Osa y")

# plt.plot(x,y1,label="$y=2x+1$") #vložení údajů do grafu
# plt.plot(x,y2,label="$y=x^2$") #syntaxe jazyka latex
# plt.plot(x,y3,label="$y=x^3$")
# plt.ylim(-1,10) #limity pro osu y
# plt.xlim(-3,3)
# plt.legend(loc="upper center") #zobrazení legendy umístění řetězcem nebo číslem 0-10
# plt.show() #zobrazení grafu a anulování všech nastavení

# x = np.arange(0,4*np.pi,0.5)
# y = np.sin(x)
# plt.plot(x,y)
# plt.show()

"""
Úkol:
1) Zobrazte graf funkce y=1/x, kde x patří do <1,10>
2) Zobrazte graf funkce y=cos(x), interval  <0,8*np.pi>
3) Vypočítejte hodnoty funkce y1=2cos(3x)-1 a 
   přidejte ji do předešlého grafu
   Oběma funkcím přidejte legendu.
4) Vygenerujte si seznam 10-ti náhodných x-vých hodnot
   a obdobný seznam y-vých hodnot. Zobrazte graf. 
5) Zobrazte graf funkce y=odmocnina(x), kde x patří do <0,1000>
"""




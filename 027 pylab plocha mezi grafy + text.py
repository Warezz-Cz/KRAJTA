# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:44:08 2012

@author: Martin
"""
"""
text (x,y,řetězec) 
     - umístí řetězec na zvolené souřadnice v grafu
     - automaticky se vkládá nad y a vpravo od x, ale způsob
       zarovnání můžeme změnit pomocí nepovinných parametrů

annotate (řetězec,xy=(x,y),xytext=(x,y),arrowprops=dict(facecolor=color,shrink=x))
     - poznámka s šipkou
     - šipka ukazuje od poznámky na bod xy
     - poznámka je umístěna na souřadnicích xytext
     - vlastnosti šipky se definují v arrowprops, shrink znamená zkrácení
       šipky v obou směrech, uvádí se jako desetinné číslo (0.25 = čtvrtina)
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-2,3,0.1)
y1=x**2-1
y2=2*x+1
plt.fill_between(x,y1,y2,where=(y2>y1), facecolor="gray")
plt.plot(x,y1,"black")
plt.plot(x,y2,"black")
# plt.text(0,0,'Popisek',fontsize="14", color="blue")

#další možné parametry pro text()
#horizontalalignment='right',verticalalignment='center'

plt.annotate('Vybarvená plocha', xy=(1,2), xytext=(1.5,-2), 
          arrowprops=dict(facecolor='red'))
plt.grid(True) 
plt.show()


"""
Úkol:
1) Nakreslete funkci y1=-(x-2)^2 + 4.
   Vykreslete přímku y2=x čárkovanou čarou.
   Vybarvěte plochu mezi oběma čarami tam, kde platí
   že (y1>y2).
   Doplňte šipku s popisem směřující přibližně na střed
   vybarvené plochy.
   Pojmenujte průsečíky čar písmeny A a B.
   Přidejte legendu s popisem obou čar.

Opakovací:
1) Vykreslete funkce y1=|sin(x)| a y2=-|sin(x)| na 
   intervalu <0,4*pi>.
   Vybarvěte plochu mezi oběma čarami světle modrou 
   barvou tam, kde platí, že (x<2*pi).
   Přidejte legendu.
   Přidejte 2 popisky se šipkou. Jeden bude patřit k
   vyplněné oblasti a druhý k nevyplněné.
2) Najděte si na internetu funkci pro vykreslení srdce
   a zkuste zobrazit její graf.
     
"""    

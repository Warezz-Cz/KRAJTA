# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:44:08 2012

@author: Martin
"""
"""
bar(x) - sloupcový graf
pie(x) - výsečový graf
"""

import numpy as np
import matplotlib.pyplot as plt

data=[10,15,8,7,12]
popisky=["USA","Řecko","Itálie","Polsko","Dánsko"]
explode = (0, 0, 0, 0.1, 0)

plt.pie(data, labels=popisky, explode=explode)

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

    
"""    

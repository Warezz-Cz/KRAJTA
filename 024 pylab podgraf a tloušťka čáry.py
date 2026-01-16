# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:34:21 2012

@author: Martin
"""
"""
subplot(x,y,z) - specifikuje, do kterého grafu v aktuálním obrázku se
                 bude kreslit (x=pocet řádků, y=pocet sloupců, z=číslo
                 grafu)
               - rozložení x a y musí být stejné  
"""

import numpy as np
import matplotlib.pyplot as plt

plt.subplot(2,2,1)
plt.plot([1,2,3,5], linewidth=4)
plt.plot([3,1,5,2])  #tyto hodnoty budou na ose y
plt.title("Graf 1")


plt.subplot(2,2,2)
plt.plot([3,2,6,2])
plt.title("Graf 2")

plt.subplot(2,2,3)
plt.plot([1,2,3,5],"y--", linewidth=4)
plt.plot([3,1,5,2])
plt.title("Graf 3")

plt.subplot(2,2,4)
plt.plot([3,2,6,2])
plt.title("Graf 4")

plt.show()


"""
Úkol:
1) Zabrazte fci y=|x-1|+1 ve dvou grafech pod sebou, 
   pokaždé jinou barvou a jinou tloušťkou.
   Použijte funkci abs().
"""

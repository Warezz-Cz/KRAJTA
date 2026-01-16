# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 08:24:01 2012

@author: Martin
"""
"""
Styly barvy:
r - červená
g - zelená
y - žlutá

Styly čar:
-  plná
:  tečkovaná
-- čárkovaná
-. čerchovaná

Styly vrcholů:
o kulaté body
^ trojúhelníčky
s čtverečky
x křížky

Kombinace (formátovací řetězce):
ro   - červená kolečka
bs:  - modré čtverečky a tečkovaná čára
g^-- - zelené trojúhelníky a čárkovaná čára
y-   - žlutá plná čára
""" 

import numpy as np
import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[1,4,9,16]

# plt.plot(x,y,"sr--") #použití formátovacího řetězce 'barvacaravrchol' na pořadí nezáleží
# plt.axis([0, 10, 0, 10]) #rozsah os x a y

# plt.plot(x,y,'b-') #vložení bodů do grafu 'barvatvar'
# plt.plot(x,y,'ro') #vložení bodů do grafu 'barvatvar'

# plt.plot(x,y,color="green")
# plt.plot(x,y,'g--',color="#ff0000") #vložení bodů do grafu 'barvatvar'

plt.show()

"""
Úkol:
1) Vykreslete graf funkce y=x**3-2*x**2+x-1 jako 
   plnou čáru s kulatými vrcholy. Rozsah volte <-5,6>.
2) Vygenerujte seznam 20-ti náhod. bodů v rovině (0,20)
   a zobrazte jej pomocí čtverečků.   
3) Načtěte z klávesnice souřadnice tří bodů a zobrazte 
   trojúhelník. Použijte funkci triplot.
"""


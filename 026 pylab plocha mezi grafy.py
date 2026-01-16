# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:17:28 2012

@author: Martin
"""
"""
fill_between(x,y1,y2) - vyplní plochu mezi dvěma čarami, druhá je
                        nepovinná
                      - lze doplnit o podmínku   
facecolor="color"     - určuje barvu výplně 
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,2*np.pi,0.1)
y1=np.cos(x)
y2=np.sin(x)
# y2=x/3

plt.plot(x,y1)
plt.plot(x,y2)

# plt.fill_between(x,y1,y2,facecolor="yellow")



# plt.fill_between(x,y1,y2,where=(y2<=0),facecolor="b")
plt.fill_between(x,y1,y2,where=(x>=4)+(x<=1),facecolor="g")

plt.grid()
plt.show()

"""
Úkol:
1) Vyplňte plochu mezi fcemi cos(x) a sin(2*x) fialovou 
   barvou v hexadecimálním tvaru na intervalu <0,2*pi>.
"""   
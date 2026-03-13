# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 07:40:31 2012

@author: Twenty
"""

# Defaultní parametry (předdefinované, implicitní)
def Vypis(x,y=5,z=6):
    print (x)
    print (y)
    print (z)

# Vypis(7,100,200)

# Pojmenované patrametry (keyword arguments)
# nezáleží na pořadí dosazení parametrů
# Vypis(z=100,x=200)




# Nepovinné parametry
# takto můžeme funkci předat libovolné množství hodnot
def Vypis2(x,*parametry):
    print (x)
    print (parametry)

# Vypis2(100,"a","b","c","další hodnota")
# Vypis2(100)



# Kombinace všech možných druhů parametrů
# Nejprve se uvádí poziční parametry (positional, nondefault)
# Pak následují předdefinované (implictní, default)
# Nakonec jsou nepovinné parametry
def PokusSParametry(x,y=1,*z):
    print (x)
    print (y)
    print (z)

# PokusSParametry(10, 20, 1, 2, 3)
# PokusSParametry(20,5,10,y=16)

"""
Úkol:
1) Napište funkci Tisk, která bude mít proměnlivý 
   počet parametrů. Všechny parametry vytiskne pod
   sebe.
2) Napište fci Soucet, která bude mít tři implicitní
   (defaultní) parametry nastavené na 0. Spočítá jejich
   součet a vrátí jej jako svůj výsledek (return).    
"""
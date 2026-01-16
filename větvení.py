import math
import os
os.system("csl")

#1)
"""
x = float(input("Zadejte první číslo: "))
y = float(input("Zadejte druhé číslo: "))

if x == y:
    print("čísla jsou stejná")
elif x > x:
    print("první číslo je větší: ")
else:
    print("první číslo je menší: ")
"""
"""

x = int(input("Zadejte celé číslo: "))

if x % 2 == 0:
    print("číslo je sudé")
else:
    print("číslo je liché")
"""
"""

x = input("Zadejte heslo: ")

if "Klokan" in x:
    print("Správné heslo")
elif "TommyHillnigger" in x:
    print("nigger"*50)
else:
    print("Ty stupidní negře vážně sis myslel že bych si zadal takové heslo")
"""
"""

a = float(input("Zadejte koeficient a: "))
b = float(input("Zadejte koeficient b: "))
c = float(input("Zadejte koeficient c: "))

dis = b**2-4*a*c


if dis == 0:
    x1 = (-b+math.sqrt(dis))/2*a
    print("rovnice má jedno řešení. ",x1)
elif dis > 0:
    x1 = (-b+math.sqrt(dis))/2*a
    x2 = (-b-math.sqrt(dis))/2*a
    print("rovnice má dvě řešení. ", x1 , ",", x2)
else:
    print("rovnice nemá řešení.")
"""
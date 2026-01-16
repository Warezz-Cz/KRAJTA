import os
os.system("cls")
import math

"""
#1

x = int(input("Zadejte číslo x: "))
y = str(input("Zadejte písmeno: "))

print(x*y)

#2

x = str(input("1. slovo: "))
y = str(input("2. slovo: "))

delkax = len(x)
delkay = len(y)

if(delkax > delkay):
    print("1. slovo je delší")
elif(delkax < delkay):
    print("2. slovo je delší")
else:
    print("Slova mají stejnou délku")

#3
    
x = float(input("Zadejte hmotnost vozidla v kg: "))

if(0 < x < 370):
    print("Vozidlo je motorka")
elif(370 <= x < 3500):
    print("Vozidlo je osobní")
elif(x >= 3500):
    print("Vozidlo je nákladní")
"""
#4
"""
r = float(input("Zadejte průměr koule v cm: "))
V = 4/3*math.pi*r**3
print("Objem koule je : ",round(V,2),"cm^3")

#5

a = float(input("Zadej stranu a: "))
b = float(input("Zadej stranu b: "))
c = float(input("Zadej stranu c: "))

if(a+b > c and b+c > a and c+a > b):
    print("trojúhelník lze sestrojit")
    if(a==b==c):
        print("Trojúhelník je rovnostranný")
    elif(a==b or b==c or c==a):
        print("Trojúhelník je rovnoramenný")
    else:
        print("Trojúhelník je různostranný")
else:
    print("Trojúhelník nelze sestrojit")
"""
#6

a = int(input("Zadejte 1. úhel: "))
b = int(input("Zadejte 2. úhel: "))
c = int(input("Zadejte 3. úhel: "))

if(a+b+c == 180):
    print("Trojúhelník existuje")
    if(a>90 or b>90 or c>90):
        print("Trojúhelník je tupoúhlý")
    elif(a<90 and b<90 and c<90):
        print("Trojúhelník je ostroúhlý")
    elif(a==90 or b==90 or c==90):
        print("Trojúhelník je pravoúhlý")
else:
    print("Trojúhelník neexistuje")
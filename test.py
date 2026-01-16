import os
os.system("cls")

A = float(input("zadej 1.číslo: "))
B = float(input("zadej 2.číslo: "))
C = float(input("zadej 3.číslo: "))

if(A > B and A > C):
    (print("1. číslo je největší"))
elif(B > A and B > C):
    (print("2. číslo je největší"))
else:
    (print("3. číslo je největší"))
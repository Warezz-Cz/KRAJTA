import os
os.system("cls")

"""
jmeno = input("zadejte jméno: ")
print("tvoje jméno je ", jmeno + ".")
"""

"""
input("pro pokračování stikni ENTER...")
print("Naschledanou v hrobě")
"""
"""
vstup =input("Zadej číslo: ")
cislo = int(vstup)
print("Dvojnásobek je", 2 * cislo)
"""
"""
a = input("Zadejte číslo: ")
cislo = int(a)
print("Zbytek po dělení je", cislo%10)
"""
"""
a = input("Délka matroša v cm: " )
b = input("Délka řezu v cm: ")

Delka = int(a)
Kus = int(b)
print("Získáte:", Delka//Kus," Kusů")
print("Odpad: ", Delka%Kus ,"cm")
"""
a = input("Ujeté kilometry: ")
b = input("Spotřebované palivo v litrech: ")
c= input("cena paliva za 1 litr: ")

Delka = int(a)
palivo = float(b)
cena = int(c)

print("náklady na cestu: ", palivo*cena ,"Kč" )
print("spotřeba na 100 km", palivo/Delka*100 ,"l/100km")
print("Náklady na 1 km", (1/Delka)*palivo*cena ,("Kč/1km"))
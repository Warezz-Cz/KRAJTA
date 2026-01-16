import math

#1
print("odmocnina", math.sqrt(8/3))

#2
odvesna1 = float(input("zadejte délku první odvěsny: "))
odvesna2 = float(input("zadejte délku druhé odvěsny: "))
Vysledek = round(math.sqrt(odvesna1**2+odvesna2**2),1)
print("přepona trojúhelníku je: ", Vysledek)

#3/4
vzdalenost = float(input("zadejta vzálenost ze které se dívate na tento krasný strom (v metrech): "))
úhel = float(input("zadejte úhel, kterým se dívate na špičku tohoto majestátního stromu (ve stupních): "))
vyska = vzdalenost*math.tan(math.radians(úhel))
print("výška stromu (v metrech) jest: ", round(vyska,1))




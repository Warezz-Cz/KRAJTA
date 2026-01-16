import os
os.system("cls")

pokus = 0
T = "monitor"
heslo = ""
while heslo != T:
    heslo = input("zadejte heslo: ")
    pokus += 1
print("počet pokusů", pokus)

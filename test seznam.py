import os
os.system("cls")
import random

print ("Seznam čísel:")
seznam=[]
for i in range(10):
    seznam+=[random.randint(0,49)]
print(*seznam)

y=0
print()
print("Pozice sudých čísel jsou:")
for prvek in seznam:
    if prvek % 2 == 0:
        print(y, end=" ")
    y+=1
        
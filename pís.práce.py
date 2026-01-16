import os
os.system("cls")
import random

i=0
while(i<20):
    y = random.randint(0,50)
    if(y % 2 == 0):
        print(y, "SUDÉ")
    else:
        print(y, "LICHÉ")
    i+=1 
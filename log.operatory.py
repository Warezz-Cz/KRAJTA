import os
os.system("cls")
"""
a = float(input("Strana a: "))
b = float(input("Strana b: "))
c = float(input("Strana c: "))
    
if((a + b > c) and (b + c > a) and (c + a > b) and (a**2 + b**2 == c**2)):
    print("Trojúhelník lze sestrojit a je pravoúhlý")
    
elif((a + b > c) and (b + c > a) and (c + a > b)):
    print("Trojúhelník lze sestrojit")

else:
    print("Trojúhelník nelze sestrojit")
"""
"""
x = float(input("souřadnice x: "))
y = float(input("souřadnice y: "))

if(x>0 and y>0): 
    print("1. kvadrant")
elif(x<0 and y>0): 
    print("2. kvadrant")
elif(x<0 and y<0): 
    print("3. kvadrant")
elif(x>0 and y<0): 
    print("4. kvadrant")
elif(x==0 and (y!=0)): 
    print("bod leží na ose y")
elif(y==0 and (x!=0)): 
    print("bod leží na ose x")
else: print("bod leží ve středu")
"""

rok = float(input("Zadejte rok: "))

if(rok % 4 == 0 and (rok % 100 !=0 or rok%400==0)):
    print("rok je přestupný")
else:
    print("rok není přestupný")
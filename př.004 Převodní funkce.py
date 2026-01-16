"""
x = float(input("desetinné číslo: "))
x = x/3
y = str(x) + " cm"
print("výsledek: ", y )
"""

a=float(input("1. rozměr: "))
b=float(input("2. rozměr: "))
c=float(input("výška: "))

rozměr = int((a+b)*2*c)

print("Na zateplení stěn je potřeba",rozměr," m^2" )

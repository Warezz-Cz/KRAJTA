# -*- coding: utf-8 -*-
"""
Formátovaný řetězec pomocí fstring
- obecný tvar je:
  retězec = f"{proměnná:specifikátor formátu}"

https://www.sallyx.org/sally/python/python3b.php#format3
https://docs.python.org/3/library/string.html#format-specification-mini-language
http://howto.py.cz/cap06.htm#17
"""
d = 25
m = 5
r = 2024

# Méně vhodný způsob
# datum = "Dnes je " + str(d) + ". " + str(m) + ". "+ str(r)
# print(datum)

#hodnoty se dosadí do řetězce dle {indexů}
# ret = f"Dnes je {d}. {m}. {r}"
# print(ret)

#doplnění datumu nulami dd.mm.rrrr
# ret = f"Dnes je {d:02}. {m:02}. {r:4}"
# print(ret)


#vložení desetinného čísla 
#(celá část je původní, desetinná se matemat. zaokrouhlí)
# ret = f"Číslo pí má hodnotu {3.14159:.3f}"
# print(ret)

#(celá část se doplní na požad. délku, desetinná se matemat. zaokrouhlí)
# ret = f"Číslo pí má hodnotu {3.14159:08.3f}"
# print(ret)


#lze uvádět různé soustavy celého čísla
# (b = binárně, x = hexadecimálně, c = znak)
# cislo = 2023
# ret = f"Číslo {cislo} je binárně {cislo:b}"
# print(ret)
# ret = f"Číslo {cislo} je hexadecimálně {cislo:x}"
# print(ret)
# kod = 65
# ret = f"Znak s kódem {kod} je znak {kod:c}"
# print(ret)

#v rámci volného prostoru můžeme obsah zarovnávat nebo i 
#vyplnit nějakým znakem, automaticky se vyplňuje mezerami
# cislo = 28
# ret = f"Číslo {cislo:<15} zarovnané doleva"
# print(ret)
# ret = f"Číslo {cislo:>15} zarovnané doprava"
# print(ret)
# ret = f"Číslo {cislo:^15} zarovnané na střed"
# print(ret)
# ret = f"Číslo {cislo:_^15} zarovnané na střed s podtržítky"
# print(ret)

"""
Úkol:
1) Vypište pod sebou 10 náhodných časových údajů ve 
   formátu hh.mm.ss.
2) Vložte číslo 42 pomocí fstringu desítkově, 
   binárně, hexadecimálně a jako znak. 
3) Spočítejte odmocninu z čísla 2 a vložte ji do
   fstringu tak, aby číslo bylo dlouhé 7 znaků, z toho
   3 za des. tečkou.
4) Vypište pod sebe 2x 10 náhodných čísel z 
   intervalu (0-1000) na 5 míst s měnou 'Kč' tak, aby:
   a) čísla ve sloupci byla zarovnána vlevo
      12   Kc
      897  Kc
      6    Kc
      ...
   b) čísla ve sloupci byla zarovnána vpravo     
        12 Kc
       897 Kc
         6 Kc
      ...   
   Nápověda: Čísla si uložíme do seznamu.
"""



    
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 10:57:07 2012

@author: Radek
"""

"""
Slovníky (dictionary, hash, asociativní pole)
- vytvářejí se pomocí {}
- položky mají tvar INDEX(KLÍČ):HODNOTA
- indexovat můžeme pomocí lib. jednoduch. dat. typu
- indexy musí být unikátní
- k hodnotám se přistupuje pomocí klíčů
- oproti seznamům mnohonásobně rychlejší přístup k datům
- není tříděný
Operace:
clear()
pop()
popitem()

"""

#Praktická ukázka
# barvy={"cervena":"#ff0000", "zelena":"#00ff00"}
# nastaveni={"sirka":80,"titulek":"Název něčeho", "mail":"xxx@neco.cz"}
# print(barvy["zelena"])       

slovnik={5:'pětka',1:"jednička",3:"trojka",2:"dvojka",4:"čtyřka"}
print (slovnik)

# Při průchodu slovníku cyklem FOR získáváme klíče!!!
# (ne hodnoty)
# for i in slovnik:
#      print (i,":",slovnik[i])

# print(*slovnik)

# vložení nového klíče a hodnoty
# klic=6
# hodnota="šestka"
# slovnik[klic]=hodnota
# print (slovnik)


# del slovnik[6]
# print (slovnik)


#keys() - vrátí seznam klíčů ze slovníku v podobě speciálního objektu
#values() - vrátí seznam hodnot v podobě speciálního objektu
#pomocí operace in zjistíme, zda je klíč uvnitř slovníku

# print (list(slovnik.keys()))
# print (list(slovnik.values()))
# print (6 in slovnik)

# x=slovnik.pop(1) #vrátí hodnotu odpovídající klíči
# print(x)
# print(slovnik)

# x=slovnik[6]
# print(x)
# x=slovnik.get(6) #vrátí hodnotu odpovídající klíči, 
# print(x)           #jinak vrátí zadanou hodnotu (0)
# print(slovnik)


# x=slovnik.popitem() #vrátí poslední vloženou dvojici
# print(x)

# slovnik.clear()
# print(slovnik)

"""
Úkol:
1) Vytvořte si jednoduchý anglicko-český překladový 
   slovník, který obsahuje 5 položek.
   Pokuste se pomocí něj překládat uživatelské vstupy,
   pokud zadané slovo nebude ve slovníku, oznamte to
   uživateli.
2) Vytvořte si slovník přátel. Klíčem budou křestní
   jména, hodnotou bude seznam osobních údajů.
   Pomocí cyklu vypište pod sebe všechny osoby ze slovníku.
   ve tvaru:
   jmeno1 => [osobní údaje]    
   jmeno2 => [osobní údaje]
   ...   
"""   




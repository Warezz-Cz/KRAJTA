import os
os.system("cls")
import random
import math

#1)
ucet = 0


def vklad(castka):  
    global ucet      
    if castka < 0:
        print("Zadali jste záporné číslo")
        input("Zkusit znovu")
        os.system("cls")
        return(False)
    else:
        ucet = ucet + castka
        print("peníze byli vloženy na učet")
        input("Stikni enter")
        os.system("cls")
        return (True)
    

def vyber(castka):
    global ucet
    if castka < 0:
        print("Zadali jste záporné číslo")
        input("Zkusit znovu")
        os.system("cls")
        return(False)
    else:
        if ucet < castka:
            print("nedostatek prostředků")
            return(False)
        else:
            ucet = ucet - castka
            input("Stikni enter")
            os.system("cls")
            return(True)
        

def zůstatek():
    global ucet
    print("Váš zůstatek: ",ucet)
    input("Stikni enter")
    os.system("cls")


while(True):
    volba=(input("1.vklad \n2.vyber \n3.zobrazit zůstatek \nVyber co checeš udělat: "))
    os.system("cls")

    if volba == '1':
        castka = int(input("Zadejte částku co chcete vložit: "))
        vklad(castka)
    if volba == '2':
        castka = int(input("Zadejte částku co chcete vybrat : "))
        vyber(castka)
    if volba == '3':
        zůstatek()
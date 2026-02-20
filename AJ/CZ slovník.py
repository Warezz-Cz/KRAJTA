import os
os.system("cls")

slovnik = {"plot":'изгородь',"negr":'негр',"tamburýna":'бубен',"kurník":'курятник',"přístup":'доступ'}
hledane_slovo=input("Zadejte slovíčko které chcete přeložit: ")

if hledane_slovo in slovnik:
    print(slovnik[hledane_slovo])
else:
    print("Ty negramotný retarde myslíš že takové slovo exituje!!!")
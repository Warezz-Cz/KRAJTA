import os
os.system("cls")
import math
import random

""" slovník={'Tomáš':'Blud','Roman':'Mlok','Adam':'DJ Eidam'}

for i in slovník:
    print(i,'=>',slovník[i]) """

DB={}
DB['Tomáš']=['Tomáš','Hegr','Krasice -','Prostějov','774 568 379']
DB['Roman']=['Jan','Roman','Svésedlická 717','Velká Bystřice','736 206 366']
DB['Maty']=['Matyáš','Volf','Posluchov 35','Posluchov','7332 183 076']
DB['Romča']=['Roman','Merta','Nový svět 84','Králová','723 399 871']
DB['Eidam']=['Adam','Rubačík','Zapadní 191','Hlušovice','-']

jmeno=0
přijmení=1
Adresa=2
mesto=3
telefon=4

""" for i in DB:
    print(DB[i]) """

""" for klic in DB:
    if DB[klic][mesto]=='Prostějov':
        print(DB[klic][jmeno],'-',DB[klic][mesto]) """

""" for i in DB:
    if DB[i][mesto]=='Prostějov':
        DB[i][mesto]='Bludov'
        print(DB[i]) """

""" for i in DB:
    DB[i] += [random.randint(45,69)]
    print(DB[i]) """







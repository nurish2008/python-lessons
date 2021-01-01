# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 12:12:41 2020

@author: Sony
"""
# tarjima = {
#     'boolean':'mantiqiy qiymat',
#     'float':'onlik son',
#     'for':'biror amalmi qayta qayta bajarish tsikli',
#     'if':'shartlarni tekshirish operatori',
#     'integer':'butun son',
#     'print':'matnni konsolga chiqarish',
#     'string':'matn',
#     'list':'royhat',
#     'tuple':'Ozgarmas royhat'
#     }
# for key, value in sorted(tarjima.items()):
#     print(f'{key.title()} ning manosi: {value}')
    
# davlatlar = {
#     'aqsh':'washington d.c',
#     'italiya':'rim',
#     'malayziya':'kuala-kumpur', 
#     'ozbekiston':'toshkent',
#     'qirgiston':'bishkek',
#     'qozogiston':'nursultan',
#     'rossiya':'moskva',
#     'singpur':'singapur',
#     'tojikiston':"dushanbe"
#     }
    
# print('Dunyo davlatlari: ')
# for davlat in sorted(davlatlar):
#     print(davlat.upper())
    
    
# print('\nDavlatlarning poytahtlari:')
# for poytaht in sorted(davlatlar.values()):
#     print(poytaht.title())


# davlatlar = {
#     'aqsh':'washington d.c',
#     'italiya':'rim',
#     'malayziya':'kuala-kumpur', 
#     'ozbekiston':'toshkent',
#     'qirgiston':'bishkek',
#     'qozogiston':'nursultan',
#     'rossiya':'moskva',
#     'singpur':'singapur',
#     'tojikiston':"dushanbe"
#     }

# country =input('Qaysi davlatning poytahtini bilishni istaysiz???..').lower()
# poytaht = davlatlar.get(country)
# if poytaht == None:
#     print("Kechirasiz bizda bu haqida ma'lumot yoq!!!")
# else:
#     print(f"{country.title()}ning poytahti {poytaht.title()} shahri")

    
taomlar = {
    'osh':20000,
    'manti':15000,
    'qozonkabob':25000,
    'lagmon':20000,
    'shashlik':10000,
    'kuksi':10000,
    'non':4000,
    'choy':2000
    }
print("Iltimos 3 ta taom zakaz qiling!!!>>>")
zakazlar = []
for menu in range(3):
    zakazlar.append(input(f"{menu+1}-taom: ").lower())
    
for zakaz in zakazlar:
    if zakaz in taomlar:
        print(f"{zakaz.title()} = {taomlar[zakaz]} som.")
    else:
        print(f"Kechirasiz bizning menuda bunday {zakaz} taomi yoq!! ")
    
    

    
    
    
    
    
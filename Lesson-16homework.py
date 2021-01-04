# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 17:41:39 2021

@author: Homework-16
"""
# 1 assignment
# buxoriy = {
#     'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#     'tyil':'810',
#     'shahar':'buxoro',
#     'vyil':60
#     }
# qodiriy = {
#     'ism':'abdulla qodiriy',
#     'tyil':'1984',
#     'shahar':'toshkent',
#     'vyil':44
#     }
# vohidov = {
#     'ism':'erkin vohidov',
#     'tyil':'1936',
#     'shahar':'fargona',
#     'vyil':80
#     }
# navoi = {
#     'ism':'alisher navoi',
#     'tyil':'1441',
#     'shahar':'xirot',
#     'vyil':60
#     }

# adabiyot = [buxoriy, qodiriy, vohidov, navoi]
# for adab in adabiyot:
#     print(f"{adab['ism'].title()}, "
#           f"{adab['tyil']}-yilda,"
#           f"{adab['shahar'].title()}da tavallud topgan."
#           f"{adab['vyil']} yil umr kurgan")

# 2 assignment

# shaxslar = {
#      'abu Abdulloh Muhammad ibn Ismoil':['Al-Jome as sahih', 'Al-adab al-mufrat',
#      'At-tarix al-kabir', 'At-tarix as-sagir'],
#      'abdulla qodiriy':['Otgan kunlar', 'Mehrobdan chayon', 'Obid ketmon'],
#      'erkin vohidov':['Tong nafasi', 'Qoshiqlarim sizga','Ozbegim', 
#      'Qiziquvchan Matsuma'],
#      'alisher navoi':['Xamsa', 'Lison ut-Tayr', 'Mahbub Al-qulub', 'Munojot']
#     }
# for ism, asarlar in shaxslar.items():
#     print(f"\n{ism.title()}ning mashxur asarlari: ")
#     for asar in asarlar: 
#         print(asar.upper())

# 3 Assignment

# kinolar = {
#     'ali':['terminator', 'rambo', 'titanic'],
#     'vali':['tenet','inception','interstellar'],
#     'hasan':['abdullajon','bomba','shaytanat'],
#     'husan':['mahallada duv-duv gap','john wick']
#     }
# for ism, movies in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari: ")
#     for kino in movies:
#         print(kino.title())
        
# davlatlar = {
#     'ozbekiston':{'poytaht':'toshkent','hududi':448978,
#                 'aholisi':33000000,
#                 'pul birligi':'som'
#                 },
#     'rossiya':{'poytaht':'moskva','hududi':17098246,
#                'aholisi':144000000, 'pul birligi':'rubl'
#                },
#     'aqsh':{'poytaht':'washington d.c','hududi':9631418,
#             'aholisi':327000000, 'pul birligi':'dollar'
#             },
#     'malayziya':{'poytaht':'kuala-lumpur','hududi':329750,
#     'aholisi':25000000, 'pul birligi':'rinngit'
#     }
#     }
# for ism, info in davlatlar.items():
#     if ism.lower()=='aqsh':
#         ism = ism.upper()
#     else:
#         ism = ism.capitalize()
#     print(f"\n{ism}ning poytahti: {info['poytaht'].title()}" 
#           f"\nHududi: {info['hududi']} kv.km."
#           f"\nAholisi: {info['aholisi']}"
#           f"\nPul birligi: {info['pul birligi']}")
    

# 4 Assignment

davlatlar = {
    'ozbekiston':{'poytaht':'toshkent','hududi':448978,
                'aholisi':33000000,
                'pul birligi':'som'
                },
    'rossiya':{'poytaht':'moskva','hududi':17098246,
               'aholisi':144000000, 'pul birligi':'rubl'
               },
    'aqsh':{'poytaht':'washington d.c','hududi':9631418,
            'aholisi':327000000, 'pul birligi':'dollar'
            },
    'malayziya':{'poytaht':'kuala-lumpur','hududi':329750,
    'aholisi':25000000, 'pul birligi':'rinngit'}
    }
davlat = input('Davlat nomini kiriting...>>').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytahti: {info['poytaht'].title()}" 
          f"\nHududi: {info['hududi']} kv.km."
          f"\nAholisi: {info['aholisi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print('Kechirasiz bizda bu davlat haqida malumot mavjud emas')
    



    
   
    
    
    





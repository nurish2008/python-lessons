# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 22:23:32 2020

@author: Sony
"""

# talaba = {
#     'ism':'alijon',
#     'familiya':'shamshiev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4 
#     }
# print(talaba.items())
# for key, value in talaba.items():
#     print(f"Kalit: {key}")
#     print(f"Qiymat: {value}\n")

# telefonlar = {
#     'ali':'iphone x pro',
#     'vali':'samsung Galaxy S20',
#     'olim':'mi 10 pro',
#     'orif':'nokia3310'
#    }
# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q.title()}")


#keys
# mahsulotlar = {
#     'oma':1000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
# print(mahsulotlar.keys())

# print("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title()) 

# print("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title()) 

# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} som")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos dokoningizga {buyum} ham olip keling!!")


#Lugat Elementlari
# print("Do'konimizdagi mahsulotlar: ")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

#print(telefonlar.values())

telefonlar = {
    'ali':'iphone x pro',
    'vali':'samsung Galaxy S20',
    'olim':'mi 10 pro',
    'orif':'nokia3310',
    'hamida':"galaxy S10",
    'maryam':'huawei p30',
    'tohir':'iphone x pro',
    'umar':'iphone x pro'
    }

print("Foydalanuvchilar quydagi telefonlarni ishlatishadi: ")
for tel in telefonlar.values():
    print(tel)

    #SET funksiyasi
print("Foydalanuvchilar quydagi telefonlarni ishlatishadi: ")
for tel in set(telefonlar.values()):
    print(tel)
 
toys = {"ball", "car", "lamp", "ball", "bear", "car"}
       
    
    
    
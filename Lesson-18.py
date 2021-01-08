# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 23:35:56 2021

@author: Sony
"""


# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n+=1
#     if javob !='ha':
#         break
# print('Dustlaringiz ruyhati quydagilar: ')
# for ism in ismlar:
#     print(ism.title())

# print("Dostlaringiz yoshini saqlaymiz")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Dostingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
    
#     javob = input('Qushimcha malumot qushasizmi? (ha/yoq)')
#     if javob == "yoq": 
#         ishora = False 
        
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")


# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# car = 'lacetti'
# while car in cars:  # toki nexia cars ro'yxati ichida ekan...
#     cars.remove(car)  # nexia ni ro'yxatdan olib tashla
    
# print(cars)

talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar[talaba] = int(baho)









# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 14:13:11 2020

@author: Sony
"""

# yosh = int(input('Yoshingiz nnechida?...'))
# if yosh<=4:
#     print('Sizga kirish bepul!!!')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# else: 
#     print('Sizga kirish 10000 so\'m')

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# else:
#     price = 10000 
# print(f'Sizga kirish {price} som')

# yosh = int(input('Yoshingiz nechida?? '))
# if yosh<=4:
#      price =0
# elif yosh<=12:
#         price = 5000
# elif yosh<=65:
#     price = 10000
# else:
#     price = 8000
# print(f'Sizga kirishi narhi {price} som')

# yosh = int(input('Yoshingiz nechida?? '))
# if yosh<=4:
#      price =0
# elif yosh<=12:
#         price = 5000
# elif yosh<=65:
#     price = 10000
# elif yosh>=70:
#     price = 8000
# print(f'Sizga kirishi narhi {price} som')

# kun = input('Bugun nima kun???>>> ')
# if kun.lower()== 'shanba' or kun.lower()== 'yakshanba':
#     print('Bugun dam olish kuni')
# else:
#     print('Bugun ish kuni')

# kun = input('Bugun nima kun???>>> ')
# harorat = float(input('Havo harorati qanday???>>> '))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print('Chomilgani ketdik... ')
# elif kun.lower()=='yakshanba' and harorat<=30: 
#     print('Uyda dam olamiz')

# narh = 15000
# choy = True
# salat = False
# if choy and salat:
#     narh = narh +10000
# elif choy or salat:
#     narh = narh + 5000
# print(f'Jami {narh} som')

# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True 
# assorti = False
# if choy:
#     print('Mijoz choy oldi.')
#     narh = narh + 3000
# if salat:
#     print('Mijoz salat oldi.')
#     narh = narh + 5000
# if non:
#    print('Mijoz non oldi')
#    narh = narh + 2000
# if kompot:
#     print('Mijoz Kompot oldi')
#     narh = narh + 5000
# if assorti:
#     print('Mijoz assorti oldi')
#     narh = narh + 15000
# print(f'Jami {narh} som')

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# 'manti' in menu 

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# 'osh' in menu

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat yeysiz???>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi. ')
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# 'manti' not in menu 

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# 'osh' not in menu 

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print('Buyurtma qabul qilindi. ')
  
# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f'Menuda {taom} bor')
#     else:
#         print(f'Kechirasiz , menuda {taom} yoq ')

menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']
if buyurtmalar:
    for taom in menu:
        print(f"Menuda {taom} bor")
    else: 
        print(f"Kechirasiz menuda {taom} yoq")
else:
        print("Savatchangiz bosh!!!")
        



    









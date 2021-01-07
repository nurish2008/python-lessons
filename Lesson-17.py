# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 22:16:03 2021

@author: While 
lesson -17
"""
# input
# ism = input('Ismingiz nima? ')
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Buyingiz nechi metr? ")
# height = float(height)

#while

# son = 1  #songa 1 qiymatni beramiz 
# while son <=5: # toki son 5 dan kichik yoki teng ekan
#     print(son, end=' ')
#     son = son + 1
#     #son +=1 #songa 1 qoshamiz
# print('Dastur tugadi')

# # while and input 

# print('Kiritilgan sonning kvadratini qaytaruvchi dastur')
# savol = 'Istalgan son kiriting? '
# savol += "(dasturni tuhtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat !='exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print('Dastur tugadi')

# Ishora 

# print('Kiritilgan sonning kvadratini qaytaruvchi dastur')
# savol = 'Istalgan son kiriting? '
# savol += "(dasturni tuhtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print("Dastur tohtadi")

# break while

# print('Kiritilgan sonning kvadratini qaytaruvchi dastur')
# savol = 'Istalgan son kiriting? '
# savol += "(dasturni tuhtatish uchun 'exit' deb yozing): "
# while True: #abadiy sikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#          print(float(qiymat)**2)
# print("Dastur tohtadi")

# break for 

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son}ning kvadrati {son**2}ga teng")
    
# continue 
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son}ning kvadrati {son**2}ga teng")

# Continue while

# son = 0
# while son<10:
#     son +=1
#     if son%2==0:
#         continue
#     else:
#         print(son)

# infinite loop

# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son) 

son = 1
while son>0:
    son += 1
    if son%2!=0:
        continue
    else:
        print(son)
        
        











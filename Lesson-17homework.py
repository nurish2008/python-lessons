# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:13:16 2021

@author: Homework lesson 17
"""
# 1- Assignment

# savol = 'Yoqtirgan kitobingizni nomini kiriting!!!'
# savol += "\n(Dasturni tuhtatish uchun 'stop' sozini yozing): "
# qiymat = ''
# while qiymat != 'stop':
#     qiymat = input(savol)
#     if qiymat != 'stop':
#         print(qiymat.title())
# print('Dastur tugadi')


# savol = 'Yoqtirgan kitobingizni nomini kiriting!!!'
# savol += "\n(Dasturni tuhtatish uchun 'stop' sozini yozing): "
# while True:
#         qiymat = input(savol)
#         if qiymat == 'stop':
#             break
#         else:
#             print(qiymat.title())
# print("dastur tugadi")


#2- Assignment

# Muzeyga chipta narhi foydalanuvchining 
# yoshiga bog'liq: 
# 7 dan yoshlarga - 2000 so'm, 
# 7-18 gacha 3000 so'm, 
# 18-65 gacha 10000 so'm, 
# 65 dan kattalarga bepul. 
# Shunday while tsikl yozingki, 
# dastur foydalanuvchi yoshini so'rasin 
# va chipta narhini chiqarsin. 
#Foydalanuvchi exit yoki quit deb yozganda 
#dastur to'xtasin (ikkita shartni ham tekshiring).

# savol = "Iltimos yoshingizni kiriting: "
# savol += "\n Dasturni tuhtatish uchun 'exit yoki 'quit' ni yozing: "
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break 
#     yosh = int(qiymat)
    
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else:
#         narh = 0
    
#     if narh == 0:
#         print ('sizga bilet tekin')
#     else:
#         print(f"Sizga chipta {narh} som buladi" )

# 3 - Assignment



savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")        
        
        
        
        
        
    



# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 23:42:58 2021

@author: Lesson-19 homework
"""

# 1- Assignment

#Foydalanuvchi ismi va yoshini so'rab, 
#uning tug'ilgan yilini hisoblaydigan funksiya yozing.

# def yosh_hisobla(ism, tyil):
#     """Foydalanuvchi ismi va yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} siz {2021-tyil} -yilda tugilgansiz")

# yosh_hisobla("Nuriddin", 40)
    

# 2- Assignment  Foydalanuvchidan son olib, 
#uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

# def kv_kub(son):
#     """ Foydalanuvchini kvadratini va kubini konsolga chiqaruvchi funksiya"""
#     print(f"{son}ning kvadrati {son**2} ga teng!\n"
#           f"{son}ning kubi {son**3} ga teng")
# kv_kub(4)

# 3 - Assignment Foydalanuvchidan son olib, 
#son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

# def juft_toq(son):
#     """ Foydalanuvchidan son olib, son juft yoki toqligini 
#     chiqaruvchi funksiya"""
#     if son%2:
#         print(f"{son} toq son")
#     else:
#         print(f"{son} juft son")
        
# juft_toq(20)
# juft_toq(23)


###
# 4-Assignment Foydalanuvchidan ikkita son olib, 
#ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
#Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

# def ikkita_son(x,y):
#     """Foydalanuvchidan ikkita son olib,kattasini chiqarish"""
#     if x>y:
#         print(f"{x}>{y}")
#     elif x<y:
#         print(f"{x}<{y}")
#     else: 
#         print(f"{x}={y}")
        
# ikkita_son(10,20)
# ikkita_son(-9,12)
# ikkita_son(115*5,5**4)

# 5- Assignment 

#Foydalanuvchidan x va y sonlarini olib, ni konsolga chiqaruvchi funksiya yozing.

# def daraja(x,y=2):
#     """Foydalanuvchidan x va y sonlarini olib, x^y  ni konsolga chiqarish"""
#     print(f"{x}niing {y} darajasi {x**2}ga teng")     

# daraja(5,2)
# daraja(3,3)
# daraja(94,4)
# daraja(6)

# 7 - Assignment

def bulinish_alomatlari(son):
    """ Foydalanuvchidan son qabul qilib,
    2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
    
    for n in range(2,11):
        if son%n:
            print(f"{son} {n}ga qoldiqsiz bulinadi")
            
bulinish_alomatlari(20)            


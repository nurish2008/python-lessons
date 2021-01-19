# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:13:30 2021

@author: Lesson-22 Homework
"""
# 1-Assignment
# =============================================================================
# Istalgancha sonlarni qabul qilib, ularning
# ko'paytmasini qaytaruvchi funksiya yozing
# =============================================================================

# def summa(*kopaytma):
#     """Kopaytmani qaytaruvchi funksiya"""
#     kupaytirish = 1
#     for kopay in kopaytma:
#         kupaytirish *=kopay
        
#     return kupaytirish

# print(summa(2,2,2))


#2-Assignment
# =============================================================================
# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi 
# funkisya yozing. Talabaning ismi va familiyasi majburiy argument, 
# qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha 
# berilishi mumkin bo'lsin.
# =============================================================================

# def talabalar_info(ism, familiya, **kwargs):
#     """talabalarning lugat kurinishida qaytaruvchi funksiya""

#     kwargs['ism']= ism
#     kwargs['familiya']= familiya
    
#     return kwargs

# tolib = talabalar_info('Nuriddin','Musaev', tyil=1980, fakultet='IT',
#                         yonalish='AT') 

# print(tolib)

def talaba_info(ism, familiya, **kwargs):
    kwargs['ism']=ism
    kwargs['familiya']=familiya
    return kwargs

talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT') 


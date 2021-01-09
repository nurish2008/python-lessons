# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 22:07:23 2021

@author: Lesson-19 Function 
"""

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalamu alaykum!!!")
    
# salom_ber()
 
###
 
# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f"Assalamu alaykum, xurmatli {ism.title()}!")
    
# salom_ber('xasan')
# salom_ber('xusan')
###

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlabchiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")

# toliq_ism('olim','hakimov')
###


# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoplaydigan dastur"""
#     print(f"{ism.title()} {2020-tugilgan_yil} yoshda")

# #yosh_hisobla('olim', 1997)- almashmaydigan usul
# yosh_hisobla(tugilgan_yil=1997, ism='olim') #bu usulda joy uzgarsa ham farqi yoo

# toliq_ism(familiya='hakimov', ism='olim')

###

def yosh_hisobla(tugilgan_yil, joriy_yil=2021):
    """Foydalanuvchi tugilgan yilidan uning yoshini hisoplaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz!!!")

#yosh_hisobla(1995,2020)
yosh_hisobla(1993)











    









       
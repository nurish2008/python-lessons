# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 23:00:23 2021

@author: Lesson-22
"""


# def summa(*sonlar):
#     """ Kiritilgan sonlar yigindisini hisoblaydigan funksiya"""
    
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son 
#     return yigindi
# print(summa(1,2))
# print(summa(1,2,3,4,5))
# print(summa(4,5,6,7))

###

# def summa(*sonlar):
#       """ Kiritilgan sonlar yigindisini hisoblaydigan funksiya"""
#       return sum(sonlar)
# print(summa(2,3))
# print(summa(1,2))
# print(summa(1,2,3,4,5))
# print(summa(4,5,6,7))

###

# def summa(x,y,*sonlar):
#     """Kiritilgan sonlarning yigindisini hisoplaydigan fuksiya"""
#     return x+y+sum(sonlar)

# print(summa(1,2))
# print(summa(1,6,4,3,2))

##

def avto_info(kompaniya, model, **malumotlar):
    """ Avto haqidagi malumotlarni Lugat kurinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya']= kompaniya
    malumotlar['model']= model
    return malumotlar

avto1 = avto_info('GM', 'Malibu', rang='qora', yil=2018)
avto2 = avto_info('Kia', 'K5', rang='qizil', narh=35000, yil=2020, korobka='avtomat')





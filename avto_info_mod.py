# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:58:14 2021

@author: Lesson-23 Modul
"""

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    """Avtomobil haqidagi malumotlarni lugat kurinishidagi funksiya"""
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

# def avto_kirit():
#     """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida malumotlarni bitta"""
#     avtolar=[]
#     while True:
#         print("\nQuydagi malumotlarni kiriting",end='')
#         kompaniya=input("Ishlab chiqaruvchi: ")
#         model=input("Modeli: ")
#         rangi=input("Rangi: ")
#         korobka=input("Korobka: ")
#         yili=input("Ishlab chiqarilgan yili: ")
#         narhi=input("Narhi: ")
        
def info_print(avto_info):
    """Avtomobillar haqida malumotlar saqlangan lugatni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()}"
          f" {avto_info['model'].upper()}, {avto_info['korobka']} korobka "
          f"{avto_info['yil']}-yil, {avto_info['narh']}$")
    
        
          
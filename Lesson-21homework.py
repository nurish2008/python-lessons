# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 22:02:50 2021

@author: Lesson-21 homework
"""

# 1-Assignment

# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].title()
        
# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)

# 2-Assinment

def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
        return matnlar
        
ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)
    

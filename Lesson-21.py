# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 22:02:54 2021

@author: Lesson -21
"""
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")        
#         baholar[ism]=int(baho)
#     return baholar 

# talabalar = ['ali','vali','hasan','husan']
# baholar = bahola(talabalar)
# print(baholar)

###

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")        
        baholar[ism]=int(baho)
    return baholar 

talabalar = ['ali','vali','hasan','husan']
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)
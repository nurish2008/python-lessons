# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:10:21 2021

@author: Lesson 20 homework
"""
# 1- Assignment

# def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {'ism':ism,
#              'familiya':familiya,
#              'tyil':tyil,
#              'yoshi':2020-tyil,
#              'tjoy':tjoy,
#              'email':email,
#              'telefon':tel}
#     return mijoz

#2-Assignment

# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar =[]
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob!='ha':
#         break
    
    

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
#           f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}") 
    
#3- Assignment

# def kattasi(x,y,z):
#     max = x
#     if y>=x:
#         max = y
#     if z>=max:
#         max=z
#     return max


# 4- Assignment

# def aylana_info(radius,pi=3.14159):
#     aylana = {"radius":radius,
#               "diametr":2*radius,
#               "perimetr":2*radius*pi,
#               'yuza':pi*radius**2}
#     return aylana


#5- Assignment

# def tub_sonlar_top(min,max):
#     tub_sonlar = []
#     for n in range(min,max+1):
#         tub = True
#         if (n==1):
#             tub = False
#         elif (n==2):
#             tub = True
#         else:
#              for x in range(2,n):
#                  if(n%x==0):
#                      tub = False
#         if tub:
#             tub_sonlar.append(n)
#     return tub_sonlar

#6 Assignment

def fibonachi(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1] + sonlar[x-2])
    return sonlar 

print(fibonachi(10))

    

    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:23:46 2021

@author: Lesson-35
"""

# yosh = input ("Yoshingizmi kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError: 
#     print('Siz butun son kiritimadingiz')
# else:
#     print(f"Siz {2021-yosh} yilda tugilgansiz")


# print('Dastur davom etayapti')
# print("dastur tugadi")

#ZeroDivisionError

# x,y=5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print('0 ga bolib bulmaydi')

#Indexerror

# mevalar = ['olma','anor','anjir','uzum']
# try: 
#     print(mevalar[4])
# except IndexError:
#     print(f"royhatda {len(mevalar)} ta meva  bor")
   
# user = {"username":"sariqdev",
#         "satus": "admin",
#         "email": "admin@sariq.dev",
#         "phone":"998712345678"} 
        
# key="tel"
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print('Bunday kalit mavjud emas')        

# print(user['username'])
    
# filename = "data.txt" #bunday file mavjud emas
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"{filename} mavjud emas")


# import json
# files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         print(f"{filename} mavjud emas")
#     else: 
#         print(talaba['ism'])
#         #fayl ustida turli amallar

# n = input('Butun son kiriting: ')
# try:
#     n = int(n)
#     x=20/n
# except ValueError: #agar foydalanuvchi butun son 
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError: 
#     print('0 ga bulib bulmaydi')
# else:
#     print(f'x={x}')



while True:
    yosh = input ("Yoshingizmi kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break
    
print(f"Siz {2021-yosh} yilda tugilgansiz")












# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 18:03:24 2021

@author: Lesson-23 modul
"""

# import avto_info_mod  - Qisqa nomga utkazish
# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "Avtomat", 2020,40000)
# avto_info_mod.info_print(avto1)

###

# import avto_info_mod as aim
# avto1 = aim.avto_info("GM", "Malibu", "Qora", "Avtomat", 2020,40000)
# aim.info_print(avto1)

###

# from avto_info_mod import avto_info, info_print
# avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2020,40000)
# info_print(avto1)

###

# from avto_info_mod import avto_info as ainfo, info_print as iprint

# avto1 = ainfo("GM", "Malibu", "Qora", "Avtomat", 2020,40000)
# iprint(avto1)

###

# from avto_info_mod import* #-Tavsiya qilinmaydi, not recomended
# avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2020,40000)
# info_print(avto1)

###

# import math

# x=400
# print (math.sqrt(x))
# print(math.pow(5,3))
# print(math.pi)
# print(math.log2(8))

###

import random as r

# #randint()  
# son = r.randint(10,100)
# print(son)

###

#Choice()
# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))

###

# x=list(range(0,51,5))
# print(x)
# print(r.choice(x))

###
# Shuffle()

x = list(range(11))
print(x)
r.shuffle(x)
print(x)







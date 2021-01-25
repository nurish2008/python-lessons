# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:25:02 2021

@author: Lesson-25 Game
"""

import random
def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1dan {x}gacha son uyladim. Topa olasizmi?", end="")
    taxminlar = 0
    while True:
        taxminlar +=1
        taxmin = int(input(">>>>"))
        if taxmin<tasodifiy_son:
            print("Xato men uylagan son bundan kattaroq. Yana harakat qiling: ", end="")
        elif taxmin>tasodifiy_son:
            print("Xato men uylagan son bundan kichikroq. Yana harakat qiling: ",  end="") 
        else:
            break
    print(f"Tabriklaymiz. {taxminlar}ta taxmin bilan Topdingiz!!!")
    return taxminlar 
    
    
def sontop_pc(x=10):
    input(f"1dan {x}gacha son uylang va istalgan tugmani bosing. Men topaman. ")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini uyladingiz: togri (t),"
                      f"Men uylagan son bundan kattaroq (+), yoki kichikroq(-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar}ta taxmin bilan Topdim barakalla!!!")
    return taxminlar 

    
def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        if taxminlar_user>taxminlar_pc:
            print("Men yutdim!!! Barakalla")
        elif taxminlar_user<taxminlar_pc:
            print("Siz yutdingiz!!!")
        else:
            print("Nichya!!!")
        yana = int(input("Yana uynaysizmi?  Ha(1)/ Yoq (0): "))
        
            
    
    
    
     
    
        
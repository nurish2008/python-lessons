# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:45:07 2021

@author: Lesson-26
"""

import random 
from uzwords import words 

def get_word():
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)
    return word.upper()
    
def display(user_letters,word):
    display_letter=""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter 


def play():
    word = get_word()  
        #Sozdagi harflar
    word_letters = set(word)
        # foydalanuvchi kiritigan harflar 
    user_letters = ''
    print(f"Мен {len(word)} хонали суз уйладим. Топа оласизми? ") 
    
    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f"Шу вактгача киритган харфларингиз: {user_letters}")
        
        
        letter = input("Харф киритинг: ").upper()
        if letter in user_letters:
            print("Бу харфни аввал киритгансиз. Бошка харф киритинг!!!")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} харфи тугри.")
        else:
            print("Бундай харф йук!")
        user_letters += letter
    print(f" Табриклаймиз! {word} сузини {len(user_letters)}та уринишда топдингиз.")
            
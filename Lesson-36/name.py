# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:53:05 2021

@author: Lesson-36
"""
def get_full_name(ism, familiya, otasi=''):
    if otasi: 
        return f"{ism} {otasi} {familiya}".title()
    else: 
        return f"{ism} {familiya}".title()

#print(get_full_name('alijon','valiev'))


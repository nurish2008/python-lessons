# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:57:38 2021

@author: Lesson-28
"""

class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        
    def get_name(self):
        return self.ism 
  
    def get_lastname(self):
        return self.familiya
        
    def get_age(self,yil):
        return yil-self.tyil
        
        
        
    def tanishtir(self):
        return(f"Ismim {self.ism} {self.familiya}, tugilgan yilim {self.tyil}")
        
talaba1 = Talaba("Olim", "Xolmirzaev",2001)
talaba2 = Talaba("Azim", "Olimov",1984)
talaba3 = Talaba("Shakar", "Shakarov",2000)


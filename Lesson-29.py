# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 21:57:46 2021

@author: Lesson-29
"""

class Talaba():
    """ Talaba nomli class yaratamiz"""
    
    def __init__(self,ism,familiya,tyil):
        """ Talabaning hususiyatlari"""
        
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        
   
    
   
    def get_info(self):
        return f"Ismim {self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"
        
    def get_name(self):
        return self.ism 
  
    def get_lastname(self):
        return self.familiya
        
    def get_age(self,yil):
        return yil-self.tyil
        
    def set_bosqich(self,yangi_bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = yangi_bosqich 
        
    def update_bosqich(self):
        """ Talabaning bosqichini 1 taga kopaytirish"""
        self.bosqich += 1 
        
        
class Fan():
    """Fan nomli klass"""
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
    
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
    
    def get_name(self):
        """Fan nomi"""
        return self.nomi
    
    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [talaba.get_fullname() for talaba in self.talabalar]
    
    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]
        
        
        
matematika = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon","Valiyev",2000)
talaba2 = Talaba("Hasan","Alimov",2001)
talaba3 = Talaba("Akrom","Boriyev",2001)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)        
        
        
        
        
        

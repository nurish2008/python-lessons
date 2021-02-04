# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:57:28 2021

@author: Lesson-30
"""

class Shaxs:
    """Shaxslar haqida maulomot"""
    def __init__(self,ism,familiya,passport,tyil):
        """Shaxsning hususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """Shaxs haqida malumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport} {self.tyil}- yilda tugilgan."
        return info
    
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning hususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        
            
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning uqish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida malumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info        

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil hususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
        
    def get_manzil(self):
        """Manzilni Korish"""
        manzil = f"{self.viloyat}-viloyati, {self.tuman}-tumani, "
        manzil += f"{self.kocha} kochasi, {self.uy}-uy."
        return manzil

talaba1_manzil = Manzil(62,"Quyosh","Olmazor","Toshkent")
talaba1 = Talaba("Musaev","Nuriddin","CA14223925",2000,"N0000012",talaba1_manzil)
    
    

    
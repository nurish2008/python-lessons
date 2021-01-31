# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 16:39:46 2021

@author: Lesson -28 homework
"""

class User:
    def __init__(self,name,username,email,mobile):
        self.name = name
        self.uname = username
        self.mail = email
        self.mobile = mobile
        
    def get_name(self):
        return self.name 
    
    def get_username(self):
        return self.username
    
    def get_mail(self):
        return self.email
    
    def get_mobile(self):
        return self.mobile
    
    def get_info(self):
        return (f"Name: {self.name}, Username: {self.uname}, e-mail:{self.mail} mobile: {self.mobile}")
    
    
user1 = User('Alijon','alijon1994','ali1994@gmail.com','998973271207')
user2 = User("Hasan","haso2000","hasan2000@gmail.com",'99897123456')
user3 = User('Nuriddin','nurish','nurish2008@gmail.com','998974454020')


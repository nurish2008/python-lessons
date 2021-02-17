# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 22:39:21 2021

@author: Lesson-33
"""


# file = open('pi.txt')
# PI = file.read()
# print(PI)
# file.close() 

# with open('pi.txt')as file:
#     pi = file.read()

# print(pi)

# pi = pi.rstrip()
# pi = pi.replace('\n','')
# pi = float(pi)
# print(pi)

# filename = 'data/talabalar.txt'
# # with open(filename) as file:
# #     for line in file:
# #         print(line)
        
        
# with open(filename) as file:
#     talabalar = file.readlines()
    
# print(talabalar)

# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)


# faylnomi = 'new_file.txt'
# ism = 'Olimjon Hasanov'
# tyil = 2004
# with open (faylnomi,'w') as fayl:
#     fayl.write(ism)
#     fayl.write(str(tyil))
    
# faylnomi = 'new_file.txt'
# ism = 'Olimjon Hasanov'
# tyil = 2004
# with open (faylnomi,'w') as fayl:
#     fayl.write(ism+'\n')
#     fayl.write(str(tyil)+'\n')

# faylnomi = 'new_file.txt'

# with open (faylnomi,'a') as fayl:
#     fayl.write('Alijon Valiev\n')
#     fayl.write('2001')
 
import pickle 

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs':2}
talaba2 = {'ism':'alijon','familiya':'valiev', 'tyil':2004, 'kurs':1}
with open ('info','wb') as file:
   
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)






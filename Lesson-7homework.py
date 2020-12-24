# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:22:30 2020

@author: Sony
"""

# ismlar = ["Abror", "Jamol", "Fayoz", "Umar", "Usmon"]
# print("Salom " + ismlar[0] + " bugun choyhona bormi?")
# print(ismlar[1] + " bugun choyhonaga boramizmi?")
# print("Dustim " + ismlar[-1] + " seni soat 6:00 da olip ketaman choyhonaga")

# sonlar = [40, 60, 10, 50, -25, 10.5, 12.5]
# print(sonlar[1] + 60)
# sonlar[5] = 15
# sonlar[-1] = 35
# del sonlar[3]
# print(sonlar)

# t_shaxslar = ['Imom Buxoriy', 'Imom Termiziy', 'Imom Muslim', 'Umar']
# z_shaxslar = ['Bill Gates', 'Jeff Bezos', 'Richard Branson', 'Ilon Mask']
# print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(0)} bilan,\n\
# zamonaviy shaxslardan esa {z_shaxslar.pop(1)} bilan\n\
# suhbat qilishni istar edim!\n")

friends = []
friends.append('Joha')
friends.append('Muzaffar')
friends.append('Komil')
friends.append('Jamol')
friends.remove('Joha')
friends.insert(0, 'Hamit')
friends.insert(3, 'Azizjon')
friends.insert(5,'Dilshod')

mexmonlar = []
mexmonlar.append(friends.pop(0))
mexmonlar.append(friends.pop(2))
mexmonlar.append(friends.pop(1))
print("\nKelgan mexmonlar: ", mexmonlar)
print("Kelmagan mexmonlar: ", friends)






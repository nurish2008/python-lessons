# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 22:13:53 2020

@author: Sony
"""

#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
#Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
# ismlar = ['Azizjon', 'Komil', 'Hamitjon', 'Jamol', 'Komol']
# for ism in ismlar:
#     print(f"Hurmatli qadrdonim {ism}, Kevotgan haftaga shukronaga kela olsanmi")
#     print("Hurmat bilan, Dusting Nuriddin\n")
#     print(f"Kod {len(ismlar)} marta takrorlandi")

#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# sonlar = list(range(11,100,2))
# for son in sonlar:
#     print(f"{son} ning kubi {son**3} ga teng")

#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.    
# kinolar = []
# print("Eng sevimli 5 ta kinolaringizni kiriting:")    
# for n in range(5):
#     kinolar.append(input(f" {n+1}-kino:"))
# print (kinolar)
    

n_suhbat = int(input("Bugun nechta kishi bilan suhbat qildingiz? >>>")
ismlar = [] 
for n in range(n_suhbat):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi? "))
print(ismlar)



    
    
    
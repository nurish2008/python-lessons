# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 00:02:51 2020

@author: Sony
"""
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
#davlatlar = ['USA', 'United Kingdom', 'Australia', 'Turkey', 'Russia', 'Japan', 'China']
#print(davlatlar)

#Ro'yxatning uzunligini konsolga chiqaring
#print("Royhatning uzunigi: ", len(davlatlar))

#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring

# print("Tartiblangan ro'yxat:", sorted(davlatlar))
# print("Asl ro'yxat o'zgarmas qoldi:", davlatlar)
# print("Teskari tartibda royhat: ", sorted(davlatlar, reverse=True))

#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
#davlatlar.sort()
#print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
#sonlar = list(range(120,1200,))
#print(sonlar)

#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# jami = sum(sonlar)
# print(sonlar)
# print("Royhatdagi sonlar yigindisi = ", jami)

#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# katta = max(sonlar)
# kichik =min(sonlar)
# print("1200 - ","120 = ",  katta - kichik)

#Ro'yxatdagi elementlar sonini hisoblang
#print(len(sonlar))

#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# print(sonlar[:20])
# print(sonlar[-20:])
#print(sonlar[530:550])

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['osh','somsa','norin','shashlik','qozonkabob']

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('qozonkabob')
nonushta.remove('osh')
nonushta.remove('norin')
nonushta.remove('shashlik')
nonushta.append('qaymoq')
nonushta.append('Tuhum')

#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
tuple(nonushta)
nonushta = list(nonushta)
nonushta[0] = 'qaymoq'
#print(nonushta)



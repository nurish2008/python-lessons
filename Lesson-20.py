# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:27:26 2021

@author: Lesson-20
"""

# def toliq_ism_yasa(ism, familiya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism

# talaba1 = toliq_ism_yasa('Olim', 'hasanov')
# talaba2 = toliq_ism_yasa('hasan', 'olimov')
# print (f" Darsga kelmagan talabalar {talaba1} va {talaba2}")
# print(f"{talaba1} Darsga kechkib keldi!!")


###

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq ism qaytaruvchi funksiya"""
    
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else: 
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()


# talaba1 = toliq_ism_yasa('Olim', 'hasanov')
# talaba2 = toliq_ism_yasa('hasan', 'olimov', 'Sadirovich')
# print (f" Darsga kelmagan talabalar {talaba1} va {talaba2}")
# print(f"{talaba1} Darsga kechkib keldi!!")

###

# def avto_info(company, model, color, korobka, year, price=None):
#     avto = {'company':company,
#           'model':model,
#           'color':color,
#           'korobka':'korobka',
#           'year':year,
#           'price':price}
#     return avto 

# avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2020)
# avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2021,15000)
# avtolar = [avto1, avto2]
# print('Online bozoridagi mavjud Avtomashinalar')
# for avto in avtolar:
#     if avto ['price']:
#         price = avto['price']
#     else:
#         price = "Nomalum"
#     print(f"{avto['color']} {avto['model']}. Narhi: {price}")

####

# def oraliq(min,max):
#     sonlar = [] 
#     while min<max:
#         sonlar.append(min)
#         min += 1 
#     return sonlar
    
# print(oraliq(0,10))
# print(oraliq(10,21))

###
        
# def oraliq(min,max,qadam):
#     sonlar = [] 
#     while min<max:
#         sonlar.append(min)
#         min += 1 
#     return sonlar
    
# print(oraliq(0,10))
# print(oraliq(10,21))        
        
        
###

def avto_info(company, model, color, korobka, year, price=None):
    avto = {'company':company,
          'model':model,
          'color':color,
          'korobka':'korobka',
          'year':year,
          'price':price}
    return avto 

print("Saitimizdagi avtolar ruyhatini shakllatiramiz")
avtolar = []
while True:
    print("\nQuydagi malumotlarni kiriting:",end='')
    company = input("Ishlab chiqaruvchi: ")   
    model= input("Model: ")
    color = input('')      
    korobka = input("Korobka: ")
    year = input("Ishlab chiqarilgan yili")
    price = ("price: " )
    avtolar.append(avto_info(company,model,color,korobka,year,price))
    javob = input("Yana avto qushasizmi? (yes/no): ")
    if javob == 'no':
        break 
    
print("\nSalonimizdagi avtolar: ")
for avto in avtolar:
    if avto['price']:
        price = avto['price']
    else:
        price = Nomalum
    print(f"{avto['rang'].title()} {avto['model'].title()} {korobka} korobka. Price:{price}")    
    



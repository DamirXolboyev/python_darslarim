# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 09:44:16 2022

10-dars

@author: Damir
"""

# yosh = int(input('Yoshingizni kiriting: '))

# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh <= 65:
#     price = 10000
# elif yosh >=70:
#     price = 8000
# print(f" Sizga kirish {price} so'm")


kun = input("Bugun kun nima?>>>")

if(kun.lower() == 'shanba' or kun.lower() == 'yakshanba'):
    print("Bugun dam olish kuni")
else:
    print("Bugun ish kuni")
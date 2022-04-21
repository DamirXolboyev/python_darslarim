# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 03:24:06 2022

@author: Shaxriyor
"""

#kocha = "Bog\'bon"
#mahalla = "Sag\'bon"
#tuman = "Bodomzor"
#viloyat = "Samarqand"


#print(f"{kocha} ko\'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

kocha=str(input("Ko\'chani kiriting:"))
mahalla=str(input("Mahallani kiriting:"))
tuman=str(input("Tumanni kiriting:"))
viloyat=str(input("Viloyatni kiriting:"))

#print(kocha.title() + " ko'chasi,\n" + mahalla.title() + " mahallasi,\n" + tuman.title() + " tumani,\n" + viloyat.title() + " viloyati")


manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)


print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 13:40:09 2022

7-dars for sikl(loop) operatori

@author: Damir
"""

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']

# for mehmon in mehmonlar:
#     print(f"Hurmatli: {mehmon}")
#     print("Sizni 25-may kuni maktabni bitirganingizga 10 yil bo\'lgani munosabati bilan bitirgan maktabingizga lutfan taklif etamiz.")
    
#     print("Hurmat bilan, maktab ma\'muryati.\n")

# sonlar = list(range(1,11))

# for son in sonlar:
#     print(f"{son} ning kvadrati  {son**2} ga teng")

# sonlar_kvadrati = []

# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
    
# print(sonlar)
# print(sonlar_kvadrati)

dostlar = []
print("5 ta eng yaqin do\'stingiz kim?")
for n in range(5):
    dostlar.append(input(f"\n{n+1}-ismni kiriting: "))
    print(dostlar)
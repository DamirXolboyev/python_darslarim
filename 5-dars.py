# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 07:35:44 2022
Ro'yhatlar №2 
 
@author: Damir
"""

#mevalar = ['olma', "o\'rik", 'behi', 'gilos']
#mevalar.remove('behi')
#print(mevalar)
#mevalar.append("shaftoli")#mevalarga shaftoli qo'shamiz

#del mevalar[1]



#print(mevalar)


#elementni sug'urib olish
# bozorlik = ["kartoshka", "piyoz", "sabzi", "un", "guruch"]
# print(bozorlik)
# bozorlik.pop(1)
# print(bozorlik)
# bozorlik.pop()
# print(bozorlik)

# ismlar = ["Zafar", "Sardor", "Jahon", "Doston", "Xayrulla"]

# xabar = "Salom " + ismlar[0] + " ishlaring yaxshimi\n"  +  ismlar[2] + " qo\'li gul usta"

# print(xabar)

sonlar = [12, -21, 3.12, 32.6, -12.8]

yig = sonlar[0] + sonlar[1]
print (sonlar)
print(yig)
sonlar[1] = 43

sonlar.remove(-12.8)

sonlar.insert(3,-65)
sonlar[2] = 13
print(sonlar)

t_shaxslar = ["Imom Al-Buxoriy", "Alisher Navoiy", "at-Termiziy", "Amir Temur"]

z_shaxslar = ["Elon Mask", "Mark Sukerberg", "Robert Kiosaki"]

b_matn = t_shaxslar.pop(1)
print(f"{b_matn}ning Xamza asari eng mashxur asarlaridan biri hisoblanadi")
i_matn = z_shaxslar.pop(1)
print(f"{i_matn} Facebookni talabalar turar joyida yaratgan hozirda unga tegishli bo\'lgan ijtimoiy tarmoqlar hammasi Metaga qarashli bo\'ldi")

friends = []

friends.append("Zafar")
friends.append("Sardor")
friends.append("Javohir")
friends.append("Jahongir")

print(friends)

friends.remove("Javohir")

print(friends)

friends.insert(0, "Doston")
friends.insert(3, "Xayrulla")
friends.insert(5, "Humoyun")

print(friends)
y_mehmonlar = []
yangi = friends.pop(0)
new = friends.pop(3)
news = friends.pop(2)
newss = friends.pop(1)


y_mehmonlar.append(yangi)
y_mehmonlar.append(news)
y_mehmonlar.append(new)
y_mehmonlar.append(newss)

print(y_mehmonlar)

#moshinlar = []
#print(moshinlar)

#moshinlar.append("Gentra")
#moshinlar.append('Tico')
#moshinlar.append("Nexia")

#moshinlar.insert(0, "Captiva")
#print(moshinlar)

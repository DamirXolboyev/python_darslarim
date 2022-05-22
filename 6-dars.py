# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:56:18 2022

Ro'yhatlarni tartiblash

@author: Damir
"""
cars = ["bmw", "mers", "audi", "ford", "volvo", "gm", "tesla"]

my_cars = cars[0:3]

new_cars = cars[:4]

old_cars = cars[3:]

print(my_cars, new_cars, old_cars)




cars.sort(reverse = True)

print(cars)
 

mehmonlar = ["Odil", "Hamid", "Temur", "Avazbek", "Farrux"]

print("sorted() qaytargan ro\'yhat: ", sorted(mehmonlar))

print("Asl ro\'yhat o\'zgarmas qoldi: ", mehmonlar)

print(sorted(mehmonlar,reverse = True))

ages = [23, 12, 10, 9, 54, 19, 7]

ages.sort()

print(ages)

print(sorted(ages, reverse = True))


fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']

fruits.reverse()

print(fruits)

print("Elementlar soni: ", len(fruits))

# sonlar = list(range(0,10))

# print(sonlar)


# juft_sonlar = list(range(0,20,2))

# print("Juft sonlar:", juft_sonlar)

# toq_sonlar = list(range(1,20,2))

# print("toq sonlar",toq_sonlar)
# sonli ro'yhat ustida sodda amal bajarish
narxlar = [12000, 21000, 32000, 45000, 10000, 4920, 54300]

arzon = min(narxlar)

qimmat = max(narxlar)

jami = sum(narxlar)

print(narxlar)

print("Eng arzon narx: ", arzon,\
      "\n Eng qimmat narx: ", qimmat,\
          "\n Jami: ", jami)
# # nusxa olish
# sonlar1 = [1, 2, 3, 4, 5]

# sonlar2 = sonlar1[:]

# sonlar2.append(6)

# sonlar2.append(7)

# print("Bu sonlar1 ro\'yhati: ",sonlar1)

# print("Bu sonlar2 ro\'yhati: ", sonlar2)

#tuple - o'zgarmas ro'yhatlar

tomonlar = (1, 2, 21.2)
print(tomonlar)

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')

toys = list(toys)

toys.append("dragon")
toys.remove("bus")

toys[1] = "mcqueen" 
toys = tuple(toys)

print(toys[1])
print(toys[-3])
print(toys[2:6])
print(toys)

""" Amaliy misol ishlash """
davlatlar = ['Canada', 'UK', 'Germany', 'Russia', 'Italy', 'Uzbekistan', 'Greece']

print(davlatlar)
davlatlar.reverse()
davlatlar.sort(reverse=True)
print(davlatlar)
print(sorted(davlatlar, reverse=True))

sonlar = list(range(120,1200,2))

yigindi = sum(sonlar)

katta = max(sonlar)
kichik = min(sonlar)
soni = len(sonlar)
ortasi = sonlar[714:734]
oxiri = sonlar[1180:]
print("Yig\'indi: ", yigindi,\
      "\nEng katta son: ", katta,\
          "\nEng kichik son: ", kichik,\
              "\nElementlar soni: ", soni,\
                  "\nboshidan 20 ta sonlar: ", ortasi,\
                      "\n oxiridan 20 ta sonlar", oxiri)
print(sonlar)

taomlar = []

taomlar.append('pelmin')
taomlar.append('jiz')
taomlar.append('tabaka')
taomlar.append('manti')
taomlar.append('osh')
print(taomlar)

nonushta = taomlar[:]

nonushta.append('yog\'')
nonushta.append('tuxum')

nonushta= tuple(nonushta)
nonushta = list(nonushta)
nonushta[0] = "qaymoq va non"
print(nonushta)




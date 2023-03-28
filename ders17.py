# LIST COMPREHENSION
# var olan listeye işlem yapmayı sağlar.

# listVal = [1,2,3,4,5]
# print(listVal)

# listVal2 = [sayi**2 for sayi in range(1,6)] # range içindeki elemanların karesini aldı.
# print(listVal2)

# div2List = [sayi for sayi in range(1,51) if sayi % 2 == 0]  # 1 ve 51 arasındaki elemanların 2 ile tam bölünenlerini yazdı.
# print(div2List)

# div6List = [sayi for sayi in range(1,51) if sayi % 2 == 0 and sayi % 3 == 0]  # 1 ve 51 arasındaki elemanların 2 ile tam bölünenlerini yazdı.
# print(div6List)
# print(len(div6List))

# meyvelerList = ['elma', 'armut', 'kavun', 'karpuz']
# meyvelerList2 = [meyve for meyve in meyvelerList]
# meyvelerList3 = [meyve.upper() for meyve in meyvelerList]
# meyvelerList4 = [meyve[0] for meyve in meyvelerList]
# meyvelerList5 = [meyve[0] for meyve in meyvelerList]
# meyvelerList5 = [meyve for meyve in meyvelerList if 'r' in meyve]
# print(meyvelerList2)
# print(meyvelerList3)
# print(meyvelerList4)
# print(meyvelerList5)
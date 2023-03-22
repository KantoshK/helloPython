# LIST DEĞİŞKENİ VE METODLARI
# SIRALANABİLİR
# DEĞİŞTİRİLEBİLİR
# INDEXLI
# YİNELENEBİLİR

# meyvelerList = ['elma', 'armut', 'kavun', 'karpuz'] # liste köşeli parantez ile oluşturulur.

# print(meyvelerList)     # listeyi yazdırır.
# print(meyvelerList[0])  # degisken[x]: listedeki 0. karakteri yazdırır.
# print(meyvelerList[1:3])  # 1'den 3' e kadar olan karakterler yazıldı.
# print(meyvelerList[-2])

# meyvelerList[1] = 'kivi' # 1. index yerine kivi yazıldı.
# print(meyvelerList)

# print(help(meyvelerList.clear)) # help(x): istediğimiz özellik için bilgi verir. (meyvelerList değişkeni yerine list'te yazabilirdik.)

# clear: listedeki elemanları siler.
# print(meyvelerList)
# print(meyvelerList.clear())

# copy: listedeki elemanları yeni değişkene kopyalar.
# print(meyvelerList)
# meyvelerListYeni = meyvelerList.copy()
# print(meyvelerListYeni)

# len: listede kaç tane eleman olduğunu yazdırır.
# print(len(meyvelerList))

# count: istediğimiz elemanın listede ne kadar olduğunu yazdırır.
# print(meyvelerList.count('elma'))

# index: istediğimiz elemanın listede kaçıncı indexte(sırada) olduğunu yazdırır.
# print(meyvelerList.index('karpuz'))

# append: veriyi ekleyip en sona atar.
# meyvelerList.append('muz')
# print(meyvelerList)

# insert: veriyi ekleyip istediğimiz indexe atar.
# meyvelerList.insert(1, 'muz')
# print(meyvelerList)

# extend: başka bir listeyi diğer listeye ekler.
# meyvelerListYeni = ['muz', 'kivi']
# meyvelerList.extend(meyvelerListYeni)
# print(meyvelerList)

# del: istediğimiz indexteki elemanı siler.
# del meyvelerList[2]
# print(meyvelerList)

# pop: istediğimiz indexteki elemanı siler ve o silinen elemanla işlem yapabiliriz.
# silinenMeyve = meyvelerList.pop(2)
# print(meyvelerList)
# print(silinenMeyve)

# remove: belirlediğimiz elemanı siler.
# meyvelerList.remove('elma')
# print(meyvelerList)

# sort: listedeki elemanları alfabeye göre sıralar.
# meyvelerList.sort()
# print(meyvelerList)

# sorted: sıralanmış listeyi yeni bir değişkene atar.
# meyvelerListSirali = sorted(meyvelerList)
# print(meyvelerListSirali)

# reverse: listedeki elemanları tersten sıralar.
# meyvelerList.reverse()
# print(meyvelerList)
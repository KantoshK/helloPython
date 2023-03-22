# SET DEĞİŞKENİ VE METODLARI
# SIRASIZ
# DEĞİŞTİRİLEBİLİR
# INDEXSIZ
# YİNELENEMEZ

# meyvelerSet = {'elma', 'armut', 'kavun', 'karpuz'}

# print(meyvelerSet)
# print(type(meyvelerSet))

# print(meyvelerSet[1]) # bu kod çalışmaz çünkü set değişkeni indexsizdir.

# print(help(set))
# print(help(set.remove))

# add: değişkene sadece 1 eleman ekler.
# meyvelerSet.add('muz')
# print(meyvelerSet) # set değişkeni indexsiz ve sırasız olduğu için eklenen eleman rastgele yerleştirilir.

# update: değişkene birden fazla eleman ekler
# meyvelerSet.update(['muz', 'kivi'])
# print(meyvelerSet)

# len: değişkende kaç tane eleman olduğunu yazdırır.
# print(len(meyvelerSet))

# remove: olan bir elemanı değişkenden kaldırır. eğer yazılan eleman değişkende yoksa hata verir.
# meyvelerSet.remove('elma')
# print(meyvelerSet)

# discard: olan bir elemanı değişkenden kaldırır. yazılan eleman yoksa yine de sıralar.
# meyvelerSet.discard('elma')
# print(meyvelerSet)

# pop: rastgele bir elemanı siler ve o silinen elemanla işlem yapabiliriz.
# silinenMeyve = meyvelerSet.pop()
# print(meyvelerSet)
# print(silinenMeyve)

# clear: değişkendeki bütün elemanları siler.
# meyvelerSet.clear()
# print(meyvelerSet)

# del: set değişkeni silinir ve bir daha kullanılamaz.
# del meyvelerSet
# print(meyvelerSet)
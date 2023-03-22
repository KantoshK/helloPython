# TUPLE DEĞİŞKENİ VE METODLARI
# SIRALANABİLİR
# DEĞİŞTİRİLEMEZ
# INDEXLI
# YİNELENEBİLİR

# meyvelerTuple = ('elma', 'armut', 'kavun', 'karpuz')

# print(meyvelerTuple)
# print(type(meyvelerTuple))

# print(meyvelerTuple[0])
# print(meyvelerTuple[1:3])
# print(meyvelerTuple[-2])

# meyvelerTuple[1] = 'kivi' # bu kod çalışmaz çünkü tuple değişkeni değiştirelemez.

# print(help(tuple))
# print(help(tuple.count))

# tuple değişkeni değiştirilemez olduğu için eleman eklenemez, çıkarılamaz ve değiştirilemez.

# len: değişkende kaç tane eleman olduğunu yazdırır.
# print(len(meyvelerTuple))

# count: istediğimiz elemanın değişkende ne kadar olduğunu yazdırır.
# print(meyvelerTuple.count('elma'))

# index: istediğimiz elemanın değişkende kaçıncı indexte(sırada) olduğunu yazdırır.
# print(meyvelerTuple.index('armut'))

# del: tuple da eleman çıkaramayız ama bu komut ile tuple değişkenini direkt silebiliriz.
# del meyvelerTuple
# print(meyvelerTuple)
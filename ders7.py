# DICTIONARY DEĞİŞKENİ VE METODLARI
# SIRASIZ
# DEĞİŞTİRİLEBİLİR
# INDEXLI
# YİNELENEMEZ

# kisiselDic = {'isim': 'ad',
#               'yaş': '10',
#               'meslek': 'iş'
# }
# print(kisiselDic)

# isimVal = kisiselDic['isim']
# print(isimVal)

# yasVal = kisiselDic['yaş']
# print(yasVal)

# kisiselDic['meslek'] = 'yazılımcı'
# meslekVal = kisiselDic['meslek']
# print(meslekVal)

# olmayan bir eleman eklenirse o eleman değişkene eklenir.
# kisiselDic['cinsiyet'] = 'erkek'
# print(kisiselDic)

# print(help(dict))
# print(help(dict.popitem))

# get: değişkende istenen keyin değerini almayı sağlar
# isimVal = kisiselDic.get('isim')
# print(isimVal)

# len: değişkende kaç tane eleman olduğunu yazdırır.,
# print(len(kisiselDic))

# pop: istediğimiz keydeki elemanı siler ve o silinen elemanla işlem yapabiliriz.
# silinenVal = kisiselDic.pop('meslek')
# print(silinenVal)

# popitem: sondaki elemanı siler ve o silinen elemanla işlem yapabiliriz.
# silinenVal = kisiselDic.popitem()
# print(silinenVal)

# del: değişken silinir ve bir daha kullanılamaz.
# del kisiselDic
# print(kisiselDic)

# clear: değişkendeki bütün elemanları siler.
# kisiselDic.clear()
# print(kisiselDic)

# dict: yeni bir sözlük tanımlamaya yarar.
# kisiselDic2 = dict(
#     isim='ad',
#     yaş='10',
#     meslek='yazılımcı'
# )
# print(kisiselDic2)
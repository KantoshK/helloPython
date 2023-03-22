# STRING METODLARI

# strVal = "merhaba dünya python"
# strVal2 = "MERHABA DÜNYA PYTHON"

# print(strVal[0])      # 0. karakter
# print(strVal[1])      # 1. karakter
# print(strVal[0:7])    # 0' dan 7'ye kadar olan karakterler
# print(strVal[-3])     # sondan 3. karakter
# print(strVal[2:-2])   # baştan 2. karakterden başlayıp sondan 3. karaktere kadar yazdırır.
# print(strVal[:3])     # baştan 3. karakter
# print(strVal[3:])     # baştan 3. karakterden sona kadar
# print(strVal[:])      # bütün karakterler yazıldı

# print(strVal.title())   # bütün baş harfler büyük yazıldı.
# print(strVal.upper())   # bütün harfler büyük yazıldı.
# print(strVal2.lower())  # bütün harfler küçük yazıldı.
# print(strVal.count('y'))# y harfinin kaç tane olduğunu yazdırır.
# print(strVal.count('python')) # python kelimesinin kaç tane olduğunu yazdırdı.
# print(strVal.find('y')) # y harfinin ilk karakter numarasını yazdırır.
# print(strVal.rfind('y'))  # y harfi sağdan aranmaya başlanır.
# print(strVal.find('z')) # eğer harf bulunamazsa çıktı "-1" şeklinde olur.
# print(strVal.replace('python', 'java')) # 1. yerine 2. yazılan yerleştirilir.
# print(strVal.istitle()) # yazıda bütün ilk harfler büyükse true, biri ya da hepsi küçükse false cevabı alınır.
# print(strVal.isupper())   # istitle komutu gibidir. bütün karakterlerin büyük olup olmadığına bakılır.
# print(strVal.islower())   # islower komutunda da bütün harflerin küçük olup olmadığına bakılır.
# print('python' in strVal) # değişkende bulunması istenen karakter var mı diye kontrol edilir. cevap true ya da false şeklindedir.

# print(len(strVal))    # len(degisken) komutunda değişkenin kaç karakter olduğu yazdılır.
# print(dir(strVal))    # değişken için kullanılabilecek komutları gösterir.

# print(help(str))       # string için gerekli yardımlar yazdırılır.
# print(help(str.replace)) # belirlenen komut için özellikler yazdırılır. (örnekte replace komutu için)
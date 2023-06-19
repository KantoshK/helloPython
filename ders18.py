# FONKSİYON, PARAMETRE VE RETURN

# Fonksiyon belli bir işlemi tek çatı altında toplayan kod bloklarıdır.
# Fonksiyonlar tekrar tekrar kullanılabilir.
# Fonksiyon belirlenir ve istendiği zaman çağırılır.

# Örnek olarak:
# def func():
#     print("Hello World")
#
# func()

# Parametreli Fonksiyonlar:
# def func(string):
#     print(string)

# def yaz(yazi):
#     print('Merhaba {}'.format(yazi))
#     print('Merhaba ' + yazi)
#
# yaz('Dünya')
# yaz('Python')

# def uslusayi(taban, us=2):
#     print(taban**us)
#
# uslusayi(2)

# RETURN: Fonksiyondan parametre alıp daha sonra kullanmaya yarar.
# Return kullanırken aldığı ilk parametreyi döndürür.
# def uslusayi(taban, us=2):
#      '''
#      Bu fonksiyon taban ve üs alır ve tabanın üssünü döndürür.
#      :param taban: İlk parametre (taban)
#      :param us: İkinci parametre (üs)
#      :return:
#      '''
#      return taban**us
#
# sonuc = print(type(uslusayi(2)))
# sonuc = print(uslusayi(2))
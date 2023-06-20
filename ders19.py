# FONKSİYON, ARGS VE KWARGS
# *ARGS: Değişken sayıda değişken alır.
# **KWARGS: Değişken sayıda değişken alır. Değişkenlerin isimleri değişkenlerle birlikte gönderilir.

# def toplam(key1, key2):
#     print(key1 + key2)
#
# toplam(10, 20)
# toplam(30, 40, 50) # Hata verir

# def func(str):
#     print(type(str))
#
# func(5) # türü: int
# func("5") # türü: str

# * ile değişkenler tuple olarak alınır.
# def func(*str):
#     print(type(str))
#
# func(5) # türü: tuple
# func("5") # türü: tuple

# def func(*argumanlar):
#     for args in argumanlar:
#         print(args)
#
# func('Hello', 'World', 'Python', 1, 2, 3)

# def toplama(*sayilar):
#     toplam = 0 # Başlangıç değeri
#     for sayi in sayilar:
#         toplam += sayi # Değişkenleri toplam değişkenine ekler.
#     print(toplam / len(sayilar)) # Toplam değişkenini sayı değişkenlerinin sayısına böler.
# # Değişkenler bir sayı olarak girilmezse hata verir.
# # toplama('a','b','c') # Hata verir.
# toplama(5,11) # Hata vermez. (0+5+11)/2 = 8

# def func(**sayilar):
#     for sayi in sayilar:
#         print(sayi)
#     for sayi in sayilar.keys():
#         print(sayi)
#     for sayi in sayilar.values():
#         print(sayi)
#     for key,val in sayilar.items():
#         print(key,"=", val)
# func(a=1, b=2, c=3) # a, b, c değerleri yazdırılır.

# def area(**values):
#     if 'a' not in values:
#         return "a değeri girilmedi." # a değeri girilmediyse hata verir.
#     elif 'b' not in values:
#         return "b değeri girilmedi." # b değeri girilmediyse hata verir.
#     else:
#         return values['a'] * values['b'] # a ve b değerleri girildiyse alan hesaplanır.

# print(area(a=5, b=10, c=15, d='tavuk')) # Eğer içinde olmayan bir değer girilirse onları görmezden gelir.

# def func(str,*args, **kwargs):
#     print(str)
#     print(args)
#     print(kwargs)
#     print(type(str)) # Türü: str
#     print(type(args)) # Türü: tuple
#     print(type(kwargs)) # Türü: dict
#
# func('Hello', 1, 2, 3, a=1, b=2, c=3)
# GLOBAL ve LOCAL
# GLOBAL: Programın her yerinde kullanılabilen değişkenlerdir.
# LOCAL: Sadece tanımlandığı blokta kullanılabilen değişkenlerdir.

# def func():
#     num = 10
# func(num) # num değişkeni tanımlı değil hatası verir.

# num1 = 10 # GLOBAL
#
# def func():
#     num2 = 10 # LOCAL
#     print(num1)
#     print(num1)

# num = 10
# def func():
#     num = 20
# func()
# print(num) # 10

# num = 10
# def func():
#     num = 20
#     print('Sayı:', num)
# func()
# print('Sayı:',num) # Sonuç olarak çıktı: Sayı: 20 Sayı: 10

# num = 10
# def func():
#     global num
#     num = 20
#     print('Sayı:', num)
# func()
# print('Sayı:',num) # Sonuç olarak çıktı: Sayı: 20 Sayı: 20
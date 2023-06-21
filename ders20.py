# LAMBDA
# Lambda: Tek satırda fonksiyon tanımlamak için kullanılır.

# def func(num):
#     return num * num

# print(func(5))
# Aynı şeyleri lambda ile yapalım.
# func = lambda num: num * num
# print(func(10))

# func = lambda num1, num2: num1 / num2
# print(func(20, 10))

# Lambda'da args kullanabiliriz.
# toplam = lambda *numbers: sum(numbers) # sum: toplama fonksiyonu
# print(toplam(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# def func(num1):
#     return lambda num2: num1 * num2

# funcIkı = func(2) # lambda num2: num2 * 2
# funcUc = func(3) # lambda num2: num2 * 3

# print(funcIkı(10))
# print(funcUc(20))

# func = lambda num, subFunc: num + subFunc(num)
# print(func(5, lambda x: x * 2)) # 5 değerini alıp lambda x: x * 2 fonksiyonuna gönderiyoruz.
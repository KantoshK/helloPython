# BOOLEAN, KARŞILAŞTIRMA VE MANTIKSAL OPERATÖRLER

# boolean: true ya da false ifadeleridir.

# boolVal = True
# print(boolVal)
# print(type(boolVal))

# boolVal = False
# print(boolVal)
# print(type(boolVal))

# boolVal1 = bool(1)  # 1: True
# boolVal2 = bool(0)  # 2: False
# print(boolVal1)
# print(boolVal2)

# print(1 == 1)   # 1, 1'e eşit olduğu için çıktı True olur.
# print(0 == 1)   # 0 ve 1 eşit olmadığı için çıktı False olur.
# print(0 != 1)   # burada 0, 1'e eşit değildir dediğimiz için çıktı True olur.

# stringlerde büyük ve küçük harfler dikkatı alınmalıdır.
# print('Merhaba' == 'Merhaba')   # True
# print('merhaba' == 'Merhaba')   # False

# print(1 > 0)    # True
# print(1 < 0)    # False
# print(0 >= 0)   # True
# print(0 >= 0)   # True
# print(0 > 0)    # False

# stringlerde alfabeye göre sıralama yapar.
# print('a' < 'a')    # False
# print('a' < 'b')    # True
# print('aa' < 'ba')  # True
# print('ac' < 'ab')  # False
# print('ab' <= 'ab') # True

# and: her ifade doğruysa True yazdırılır.
# print(1 == 1 and 0 == 0)

# or: ifadelerden en az birisi doğruysa True yazdırılır.
# print(1 == 1 or 0 == 1)

# not: sonucu tam tersine çevirir. (ifade True ise False yazdırır. ifade False ise True yazdırır.)
# print(not(0 < 1))   # aslında ifade true ama not ile false yazdırıldı.
# print(not(1 < 0))   # aslında ifade false ama not ile true yazdırıldı.

# NOT: öncelikler parantez ile belirtilir